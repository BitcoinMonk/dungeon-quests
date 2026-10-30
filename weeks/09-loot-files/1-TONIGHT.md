# Week 9 · Loot Files — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/09-loot-files`

**Start the week:** merge last week's pull request together, then `git checkout master`, `git pull`, `git checkout -b week-09`

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

Real programs work with **data**: files that are way too big to read with your eyes.
`loot.txt` is a dragon's hoard with hundreds of items, one per line. Python can read it in a blink and turn it into a list.

This is how **Advent of Code** works, a real puzzle contest programmers do every December: you get a big input file and write code to find one answer.

## Steps

### 1. Look at the data (5 min)
Open `loot.txt` in VS Code. Scroll. How many lines do you think there are? Could you count the gems by hand?

### 2. Predict (5 min)
Open `loot.py`. What will it print? Don't worry about understanding the first line yet.

### 3. Run and investigate (20 min)
1. Run it. Was your guess about the number of lines close?
2. The first line does three things, read right to left:
   - `open("loot.txt")` opens the file
   - `.read()` reads all of it as one giant string
   - `.splitlines()` chops it into a list, one item per line
3. What's `lines[:5]`? Try `lines[:10]` and `lines[-3:]`. (This is called **slicing**.)
4. Change the loop to go over **all** the lines. Scroll the output. That's a lot of loot.

### 4. Together: count the candles (20 min)
At the bottom of `loot.py`, write code together that counts how many lines are `"candle"`.
The pattern is one you'll use forever:
```python
count = 0
for thing in lines:
    if thing == "candle":
        count = count + 1
print(count)
```
Talk through it: why does `count = 0` go **before** the loop? What happens if you put it inside?

### 5. Look ahead (5 min)
Read `2-THIS-WEEK.md`. Three puzzles use this file.

## New words

| Word | Meaning |
|---|---|
| **file** | Data saved on the computer. Your code can read it. |
| **`.splitlines()`** | Chops a big string into a list of lines. |
| **slice** | Part of a list: `lines[:5]` is the first five. |
| **input file** | The data a puzzle gives you. |
| **accumulator** | A variable you build up in a loop, like `count` or `total`. |

---

## Mentor notes
- `open("loot.txt")` looks in the folder the terminal is in. `FileNotFoundError` means he isn't in `weeks/09-loot-files`; `cd` there and run it again.
- The count-in-a-loop pattern is the single most reused idea in the rest of the course. Make sure he can write it without looking.
- **Ready check:** *From a blank file, read `loot.txt` and count how many lines are "rat".*
