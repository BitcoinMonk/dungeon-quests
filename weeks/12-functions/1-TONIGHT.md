# Week 12 · Functions — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/12-functions`

**Start the week:** merge last week's pull request together, then `git checkout main`, `git pull`, `git checkout -b week-12`

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

You've been **using** functions since week 1: `print()`, `input()`, `len()`, `random.randint()`. Tonight you **make** your own.
A function is a little machine: you give it something (**parameters**), it does a job, and it can hand something back (**return**).
```python
def roll(sides):
    return random.randint(1, sides)
```
Now `roll(6)` rolls a 6-sided dice, and `roll(20)` rolls a 20-sided one.

## Steps

### 1. Predict (10 min)
Open `dice.py`. Python reads it top to bottom, but the `def` blocks **don't run** until they're called.
Which line actually runs first? What will the program print?

### 2. Run (5 min)
Run it a few times. Try typing `axe` when it asks for a weapon.

### 3. Investigate (20 min)
1. In `announce("The hero", roll(6))`, which runs first, `roll` or `announce`? Why?
2. What's the difference between `roll` and `announce`? One **returns** a value, one **prints**. Try `x = announce("Bob", 3)` then `print(x)`. What's in `x`?
3. `ask` has a `while True` loop but no `break`. How does it stop? (`return` leaves the function immediately.)
4. Why is `ask` useful? Think about how many times you've written "ask a question until the answer is OK" this course.

### 4. Make together (15 min)
Write a new function together:
```python
def heal(health, amount):
```
It should **return** the new health, but never more than 20. Test it:
```python
print(heal(15, 3))   # should be 18
print(heal(15, 10))  # should be 20, not 25
```

## New words

| Word | Meaning |
|---|---|
| **function** | A named chunk of code you can run whenever you want. |
| **`def`** | "Define": make a new function. |
| **parameter** | An input the function needs, like `sides`. |
| **call** | Run a function: `roll(6)`. |
| **`return`** | Hand a value back and leave the function. |
| **print vs return** | `print` shows it to the **player**. `return` gives it back to the **code**. |

---

## Mentor notes
- `print` vs `return` is the classic confusion. If he writes a function that prints when it should return, ask "can the rest of your code *use* that number?"
- The `'/'.join(options)` bit in `ask` is new. If he asks, it glues a list into one string with `/` between items. Otherwise, it's fine to treat it as magic for now.
- **Ready check:** *From a blank file, write a function with a parameter that returns something, call it twice, and explain print vs return.*
