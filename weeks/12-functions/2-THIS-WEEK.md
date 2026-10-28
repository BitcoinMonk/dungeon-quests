# Week 12 · Functions — This week, on your own

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 12.1 🔧 Many dice
In `dice.py`, write `roll_many(count, sides)`. It rolls `count` dice and **returns** the total.
`roll_many(3, 6)` should give a number from 3 to 18. Hint: use a `for` loop and your `roll` function.
- [ ] Done

### 12.2 🔧 Doors, but tidier
Copy `doors.py` from week 4 into this folder. Copy the `ask` function into it, and use `ask` for the door question.
What happens now if the player types something silly?
- [ ] Done

### 12.3 🔮 Function puzzles
Make `func_predict.py` and **predict** the output before running:
```python
def double(n):
    return n * 2

def shout(word):
    print(word.upper() + "!")

print(double(4))
print(double(double(3)))
shout("run")
x = double(5) + double(1)
print(x)
y = shout("hide")
print(y)
```
What is `y`, and why?
- [ ] Done

### 12.4 🧩 Lucky numbers
In the wizard's world, a number is **lucky** if it can be divided by 7 with nothing left over, **or** if its last digit is 7.
(Hint: `n % 7 == 0` and `n % 10 == 7`.)
Write a function `is_lucky(n)` that returns `True` or `False`. Then use a loop to find:
**how many lucky numbers are there from 1 to 1000?** Check your answer.
- [ ] Done

### 12.5 🛠️ Your dungeon toolbox
New blank file: `toolbox.py`. Write three functions you think your own dungeon will need, and test each one.
Ideas: `describe(room)`, `show_inventory(items)`, `attack(attacker, defender)`, `is_dead(monster)`.
- [ ] Done

---

### ⭐ Stretch
- Write `ask_number(question, low, high)` that keeps asking until the player types a whole number between `low` and `high`, then returns it as an `int`. (What happens with `int("abc")`? You'll need to check the text first; look up `.isdigit()`.)
