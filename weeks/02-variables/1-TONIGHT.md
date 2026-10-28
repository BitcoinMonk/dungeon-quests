# Week 2 · Variables — Tonight's lesson

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

A **variable** is a name with a value stuck to it, like a labelled box.
`gold = 5` means: "make a box called `gold` and put 5 in it."
Games are full of variables: health, gold, score, level.

## Steps

### 1. Predict (10 min)
Open `hero.py`. **Don't run it yet.**
On paper, write what you think every line of output will be, in order.

### 2. Run (5 min)
Press ▶. Compare with your paper. Circle anything you got wrong and talk about why.

### 3. Investigate (15 min)
Answer these out loud with your mentor:
1. `gold = gold + 10`: how can gold equal gold plus 10? (Hint: Python works out the **right side first**, then puts the answer in the box on the left.)
2. Why does `"Grimble"` have quotes but `20` doesn't?
3. What happens if you write `print("name")` instead of `print(name)`? Predict, then try.
4. In `print("Hero:", name)`, what does the comma do?

### 4. Modify together (15 min)
1. Add a variable `level = 1` near the top and print it.
2. After the trap, the hero levels up: make `level` go up by 1 and print it.
3. Try these in the code and predict each first:
   ```python
   print(health * 2)
   print(gold - health)
   print(10 / 4)
   ```

### 5. Look ahead (5 min)
Read through `2-THIS-WEEK.md` together.

## New words

| Word | Meaning |
|---|---|
| **variable** | A name that holds a value: `gold = 5`. |
| **`=`** | "Put the right side into the left side." Not "equals" like in maths. |
| **integer** | A whole number: `20`. No quotes. |
| **string** | Text: `"Grimble"`. Always in quotes. |
| `+  -  *  /` | Add, subtract, multiply, divide. |

---

## Mentor notes
- The big misconception this week is reading `=` as "is equal to". Keep saying "put into".
- If he mixes up `print("name")` and `print(name)`, that's the lesson working. Let him find it.
- **Ready check:** *Explain what `gold = gold + 10` does in his own words, and write a 3-line program from a blank file that makes a variable, changes it, and prints it.*
