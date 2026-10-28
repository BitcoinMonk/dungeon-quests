# Week 8 · Lists — Tonight's lesson

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

So far each variable holds **one** thing. A **list** holds lots of things in one variable, in order:
```python
backpack = ["torch", "rope", "bread"]
```
That's how the week 1 dungeon kept your inventory.

## Steps

### 1. Predict (10 min)
Open `backpack.py`. Don't run it. Write down every line it will print.
Careful with `backpack[0]`: what do you think the 0 means?

### 2. Run (5 min)
Check your predictions. Which ones were wrong?

### 3. Investigate (20 min)
1. Python counts list positions from **0**, not 1. What's `backpack[1]`? `backpack[2]`? Try them.
2. What happens with `backpack[10]`? Read the error.
3. What do you think `backpack[-1]` gives you? Try it.
4. The `for thing in backpack:` loop: what is `thing` the first time around? The second time?
5. What happens if you `remove` something that isn't in the list? Predict, then try.

### 4. Modify together (15 min)
Add these to the end of `backpack.py`, predicting each one first:
```python
backpack.append("map")
backpack.append("map")
print(backpack)
print(backpack.count("map"))
backpack.sort()
print(backpack)
```

## New words

| Word | Meaning |
|---|---|
| **list** | Many values in one variable: `[1, 2, 3]`. |
| **index** | A position in a list. Starts at **0**. `backpack[0]` is the first thing. |
| **`len(x)`** | How many things are in the list. |
| **`.append(x)`** | Add to the end. |
| **`.remove(x)`** | Take out the first one that matches. |
| **`x in list`** | True if x is in the list. |
| **`for thing in list:`** | Loop once for each thing in the list. |

---

## Mentor notes
- Counting from 0 is weird for everyone. Don't rush it.
- This is the first week where he can go back and read real parts of `dungeon.py` (`inventory.append(item)`, `"key" not in inventory`). Show him.
- **Ready check:** *From a blank file, loop over a list of numbers and count how many are bigger than 10.*
