# Week 4 · Decisions — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/04-decisions`

**Start the week:** merge last week's pull request together, then `git checkout master`, `git pull`, `git checkout -b week-04`

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

Games are all about choices. `if` lets your program **choose** what to do based on what's true right now.

```python
if choice == "red":
    print("fire!")
```
Read it as: "**if** choice is red, **then** do the indented lines."

## Steps

### 1. Predict (10 min)
Open `doors.py`. Don't run it. On paper, write what it prints if the player types:
1. `red`
2. `blue`
3. `purple`
4. `Red` (capital R)

### 2. Run (10 min)
Try all four. Which one surprised you? Why did `Red` do that?
(Python is picky: `"Red"` and `"red"` are different strings.)

### 3. Investigate (15 min)
1. Why `==` (two equals) and not `=`? Swap one to `=` and run it. Read the error.
   `=` *puts* a value in a variable. `==` *asks* "are these the same?"
2. Why are some lines pushed in (**indented**)? Remove the spaces in front of one `print` under the `if` and run it.
3. Which line runs **no matter what** door you pick? How can you tell?
4. What's the difference between `if`, `elif` and `else`?

### 4. Modify together (20 min)
1. Add a **green** door with your own outcome. You need a new `elif`.
2. Fix the capital-letter problem. Change the input line to:
   ```python
   choice = input("Which door? (red/blue) ").lower()
   ```
   Predict: what does `.lower()` do? Test with `RED`.

## New words

| Word | Meaning |
|---|---|
| **`if`** | Run the indented lines only when something is true. |
| **`elif`** | "Else if": check this next, if the earlier ones weren't true. |
| **`else`** | When none of the above were true. |
| **`==`** | "Is it the same?" Compare, don't assign. |
| **indent** | The spaces at the start of a line (4 spaces or Tab). They show which lines belong to the `if`. |
| **`.lower()`** | Turns a string into all lowercase. |

---

## Mentor notes
- `=` vs `==` and indentation are the two classic bugs here. Make him hit both on purpose tonight so he recognizes them later.
- **Ready check:** *From a blank file, write an `if / elif / else` that reacts to something the player types, with correct indentation, without looking.*
