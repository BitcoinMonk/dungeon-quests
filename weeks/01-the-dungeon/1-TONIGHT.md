# Week 1 · The Dungeon — Tonight's lesson

**Together with your mentor, about 90 minutes.** You drive the keyboard.

## Tonight's idea

A program is just a text file full of instructions. The computer reads them **top to bottom** and does each one.
Tonight you play a game, then you open it up and change it.

## Steps

### 1. Set up (30 min)
Follow **Setup** in the main [README](../../README.md). Finish when the game starts.

### 2. Play (15 min)
Open `dungeon.py` and press ▶. Play until you win or get eaten. You'll probably get eaten. That's fine, play again.

### 3. Look inside (15 min)
Scroll through `dungeon.py` together. Don't try to understand it all. Just find:
- The line that prints `DUNGEON QUEST`.
- The description of the library.
- Where the goblin shows up.

Lines starting with `#` are **comments**. Python skips them; they're notes for humans.

### 4. Predict, then change (20 min)
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

## New words

| Word | Meaning |
|---|---|
| **program** | A file of instructions the computer follows. |
| **run** | Tell the computer to follow the instructions (the ▶ button). |
| **`print`** | Shows text on the screen. |
| **string** | Text inside quotes, like `"hello"`. |
| **comment** | A `#` line Python ignores. A note for humans. |
| **error** | Python telling you it got confused, and where. |

---

## Mentor notes
- **Setup is the risky part.** On Windows, if ▶ does nothing or says Python isn't found, re-run the Python installer and tick "Add to PATH", then restart VS Code.
- Let him get eaten by the goblin. Finding out *why* (no sword) is the first piece of debugging.
- **Ready check** (ask at the start of next evening): *Open a file, run it, and change what one `print` line says, without help. When there's an error, point to the line number it names.*
