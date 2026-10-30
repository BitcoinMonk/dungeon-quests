# Week 3 · Input and Math — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/03-input-and-math`

**Start the week:** merge last week's pull request together, then `git checkout main`, `git pull`, `git checkout -b week-03`

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

Until now your programs just talked. Tonight they **listen**.
`input()` stops the program, waits for the player to type something, and gives you what they typed.

## Steps

### 1. Predict (10 min)
Open `shop.py`. Don't run it.
If the player types `2`, what will the last line print? Write it down. What if they type `4`?

### 2. Run (5 min)
Run it a few times with different numbers. Were your predictions right?

### 3. Investigate (20 min)
1. Put a `#` at the start of the line `how_many = int(how_many)` so Python skips it. Run it. Read the error.
   `input()` always gives you a **string** (text), even if the player types a number. `int()` turns `"2"` into `2`. Take the `#` away again.
2. What's different about the last `print`? It has an `f` before the quotes and `{ }` inside.
   That's an **f-string**: anything in `{ }` gets swapped for the variable's value. Try changing it to:
   ```python
   print(f"You bought {how_many} potions!")
   ```
3. Predict, then try each of these in a new file `math_test.py`:
   ```python
   print(17 // 5)
   print(17 % 5)
   print(2 ** 3)
   ```
   `//` divides and throws away the leftover. `%` gives you **only** the leftover. `**` means "to the power of".

### 4. Modify together (15 min)
Make the shop ask for the player's name at the start and greet them by name, using an f-string.

## New words

| Word | Meaning |
|---|---|
| **`input()`** | Waits for the player to type, gives back what they typed (as a string). |
| **`int()`** | Turns a string like `"42"` into the number `42`. |
| **f-string** | `f"Hi {name}"`: a string with variables slotted in. |
| **`//`** | Divide, drop the leftover. `17 // 5` is `3`. |
| **`%`** | Just the leftover. `17 % 5` is `2`. |

---

## Mentor notes
- The `input`-gives-a-string idea trips everyone up. The error from step 3.1 is the best teacher, so let him read it fully.
- `//` and `%` are worth the time: they come back in puzzles all the time.
- **Ready check:** *From a blank file, write a program that asks for a number, does math with it, and prints the result in an f-string.*
