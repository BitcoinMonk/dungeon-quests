# Week 7 · For Loops — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/07-for-loops`

**Start the week:** merge last week's pull request together, then `git checkout master`, `git pull`, `git checkout -b week-07`

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

`while` loops until something changes. `for` loops **a set number of times**.
```python
for step in range(1, 11):
```
means: "do this with `step` = 1, then 2, then 3… up to 10." (It stops **before** 11.)

Tonight you also put everything together into a real **battle loop**.

## Steps

### 1. Predict: stairs (5 min)
Open `stairs.py`. How many lines will it print? What's the first step number? The last?

### 2. Run and investigate: stairs (15 min)
1. Run it. Why does it stop at 10 and not 11?
2. Predict, then try each change:
   - `range(1, 101)`
   - `range(5)`, which only has one number. Where does it start?
   - `range(0, 20, 2)`, which has a third number. What does it do?
   - `range(10, 0, -1)`
3. Inside the loop, change the print to `print("Step", step, "of 10")`.

### 3. Predict: battle (5 min)
Open `battle.py`. Read it together.
- When does the `while` loop stop? There are **two** ways.
- Why is there a `break` after the goblin's health check?

### 4. Play and investigate: battle (15 min)
1. Play it 3 times. Did you ever lose?
2. Delete the `if goblin_health <= 0: break` lines (two lines). Play again. What weird thing can happen now? Put them back.
3. Find every place the code uses something from an earlier week: variables, `input`, `if`, `random`, f-strings, `while`.

### 5. Modify together (15 min)
Make the goblin tougher: 25 health, bites for 2 to 5. Is the fight still fair? Change the numbers until it feels exciting.

## New words

| Word | Meaning |
|---|---|
| **`for`** | Loop once for each thing, like each number in a range. |
| **`range(a, b)`** | The numbers from a up to (but **not including**) b. |
| **loop variable** | The name after `for`, like `step`. It changes every time around. |
| **game loop** | The main loop that keeps a game running until it ends. |

---

## Mentor notes
- "Up to but not including" is an off-by-one trap. Have him predict ranges until it clicks.
- Rule of thumb to share: use `for` when you know how many times, use `while` when you don't.
- **Ready check:** *Use a `for` loop to add up the numbers 1 to 10 into a `total` variable, from a blank file.*
