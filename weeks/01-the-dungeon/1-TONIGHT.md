# Week 1 · The Dungeon — Tonight's lesson

**Together with your mentor, about 90 minutes.** You drive the keyboard.

## Tonight's idea

A program is just a text file full of instructions. The computer reads them **top to bottom** and does each one.
Tonight you play a game, then you open it up and change it. You also start using **Git**, the tool programmers use to save their work and hand it in.

## Steps

### 1. Meet the terminal and Git (20 min)
The **terminal** is where you type commands to the computer. Programmers use it all day.
Open the `dungeon-quests` folder in VS Code, then open the terminal with **Terminal → New Terminal**.

1. Type `ls` to see the files in the main folder.
2. Tell Git who you are. You only do this once, ever:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "the email on your GitHub account"
   git config --global push.autoSetupRemote true
   ```
3. Get the newest version of the course:
   ```
   git pull
   ```
4. Make your own **branch** for this week, a separate workspace for your changes:
   ```
   git checkout -b week-01
   ```

Keep [GIT.md](../../GIT.md) open in another tab. It has every Git command you need.

### 2. Play (15 min)
1. Go into this week's folder:
   ```
   cd weeks/01-the-dungeon
   ```
   Try typing just `cd weeks/01` and pressing **Tab**. The terminal finishes the name for you.
2. Run the game:
   ```
   python dungeon.py
   ```
Play until you win or get eaten. You'll probably get eaten. That's fine. Press **↑** to bring back `python dungeon.py` and play again.

### 3. Look inside (10 min)
Scroll through `dungeon.py` together. Don't try to understand it all. Just find:
- The line that prints `DUNGEON QUEST`.
- The description of the library.
- Where the goblin shows up.

Lines starting with `#` are **comments**. Python skips them; they're notes for humans.

### 4. Predict, then change (15 min)
1. Find `print("You wake up on a cold floor. Your head hurts.")`.
   **Predict:** if you change the words inside the quotes, what will the game show? Say it out loud.
2. Change it. Run. Were you right?
3. Now add a brand new line right under it:
   ```python
   print("Somewhere, a rat laughs at you.")
   ```
   Predict where it will show up. Run.

### 5. Break it (10 min)
Delete the last `"` from one of the `print` lines and run it. You get an **error**.
- Read the **last line** of the error. What does it say?
- Which **line number** does it point to?

Put the `"` back. Errors are normal. Programmers see them all day.

### 6. Save a commit (10 min)
A **commit** is a save point. Git remembers exactly what every file looked like.
```
git status
git diff
git add -A
git commit -m "1.0 new opening line"
```
- `git status` lists the files you changed.
- `git diff` shows exactly which lines changed: red is old, green is new. Press **q** to get out.
- `git add -A` picks up all your changes, and `git commit` saves them with a message.

From now on, commit **every time you try something**, even when it's broken. Broken commits are fine on your branch: they show how you got there.

## New words

| Word | Meaning |
|---|---|
| **program** | A file of instructions the computer follows. |
| **terminal** | The window where you type commands to the computer. |
| **`cd`** | "Change directory": move into a folder. `cd ..` goes up one folder. |
| **run** | Tell the computer to follow the instructions: `python dungeon.py`. |
| **`print`** | Shows text on the screen. |
| **string** | Text inside quotes, like `"hello"`. |
| **comment** | A `#` line Python ignores. A note for humans. |
| **error** | Python telling you it got confused, and where. |
| **Git** | Keeps save points of your work. |
| **branch** | Your own workspace for a set of changes, like `week-01`. |
| **commit** | One save point, with a message saying what changed. |

---

## Mentor notes
- **Before `git pull`:** run `git status`. If it lists files he changed before tonight, either commit them on a branch or throw them away with `git restore .` first, otherwise the pull can refuse.
- He needs a GitHub account, and you need to add him as a collaborator before next week (see [MENTOR.md](../../MENTOR.md)).
- If `python` says it isn't found or opens the Microsoft Store, Python isn't on the PATH: re-run the installer, check "Add python.exe to PATH", then reopen VS Code.
- `cannot find path` or `No such file` almost always means he's in the wrong folder. The terminal's prompt shows where he is.
- Let him get eaten by the goblin. Finding out *why* (no sword) is the first piece of debugging.
- **Ready check** (ask at the start of next evening): *`cd` into a week's folder, run a file, and change what one `print` line says, without help. When there's an error, point to the line number it names. Make a commit without looking at GIT.md.*
