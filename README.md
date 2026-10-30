# Dungeon Quests

Learn to code by building a dungeon adventure game in Python, one week at a time.
In the last weeks you'll write your own dungeon from a blank file, and your mentor will try to beat it.

## How it works

Every week has its own folder in `weeks/`. Inside each one:

| File | What it is |
|---|---|
| **`1-TONIGHT.md`** | The lesson you do **together with your mentor** on your evening. |
| **`2-THIS-WEEK.md`** | Quests to do **on your own** during the week. One or two a day is plenty. |
| `.py` files | The code the lesson and quests use. |

You save your work with Git and hand in each week as a pull request: **[GIT.md](GIT.md)** has every command.
Track where you are in **[PROGRESS.md](PROGRESS.md)**. Mentors: start with **[MENTOR.md](MENTOR.md)**.

## The rules

1. **One week at a time.** Don't open next week's folder until this week's pull request is merged. Finished early? Do the ⭐ stretch quests.
2. **Type it yourself.** Don't copy and paste code. Your fingers learn too.
3. **Predict before you run.** Every time. Say or write what you think will happen, *then* run it.
4. **Errors are clues, not failures.** Read the last line of the error and find the line number it points to.
5. **AI is a tutor, not a typist.** Ask it to explain things or give you a hint. Never ask it to write your code. A good question: *"Don't give me the code. Give me a hint about why this doesn't work:"* and paste your code.
6. **Stuck for 20 minutes?** Write down what you tried, move on to the next quest, and bring it to your next evening.

## Quest types

| | Type | What you do |
|---|---|---|
| 🔮 | **Predict** | Work out what code will do *before* you run it. Write your guess down. |
| 🔧 | **Modify** | Change code that already works to make it do something new. |
| 🧩 | **Puzzle** | Use code to find an answer, then check it with `check.py`. |
| 🛠️ | **Make** | Write something new, starting from a blank file. |

Keep a **notebook** (paper is great) for predictions, maps and things you got stuck on.

## Running your code

You run everything from the **terminal** at the bottom of VS Code. Open it with **Terminal → New Terminal**. It starts in the main `dungeon-quests` folder.

1. Go into a week's folder with `cd` ("change directory"):
   ```
   cd weeks/01-the-dungeon
   ```
2. Run a file by typing `python` and the file's name:
   ```
   python dungeon.py
   ```
3. To switch to a different week, go back up to the main folder first (`..` means "the folder above"), then into the new week:
   ```
   cd ../..
   cd weeks/02-variables
   ```

Tips:
- Type part of a name, like `cd weeks/02`, and press **Tab**. The terminal finishes it for you.
- `ls` lists the files in the folder you're in.
- Press **↑** to bring back your last command, so you don't have to retype `python hero.py` every time.
- A program stuck in a loop? Click in the terminal and press **Ctrl+C**.
- On a Mac, type `python3` instead of `python`.

## Checking a 🧩 puzzle answer

`check.py` lives in the main folder. From inside a week's folder, run:
```
python ../../check.py
```
It asks for the quest number (like `2.5`) and your answer.

## Getting the project (week 1, with your mentor)

1. Open a terminal and download the project:
   ```
   git clone https://github.com/BitcoinMonk/dungeon-quests.git
   ```
2. In VS Code: **File → Open Folder…** and pick the `dungeon-quests` folder. If it asks to install the **Python extension**, say yes.
3. Open the terminal (**Terminal → New Terminal**) and type:
   ```
   cd weeks/01-the-dungeon
   python dungeon.py
   ```
   If a game starts, you're ready.
