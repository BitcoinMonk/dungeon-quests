# Week 5 · More Decisions — Tonight's lesson

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

Two new tools:
- **Comparing numbers**: `<`, `>`, `<=`, `>=`. Remember the shop that let you go broke? Tonight you fix it.
- **Randomness**: `random.randint(1, 6)` rolls a dice. Every game needs some luck.

## Steps

### 1. Predict: the shop (10 min)
Open `shop2.py`. You have 30 gold and potions are 7 each.
On paper: what happens if you buy **4**? What about **5**? Then run both and check.

### 2. Investigate: the shop (10 min)
1. What does `cost <= gold` mean in plain English?
2. What happens if you change `<=` to `<`? Is there a number of potions where that changes the answer? (Try changing `gold` to 28.)

### 3. Predict: the fight (5 min)
Open `fight.py`. There are three different things that can happen. Which roll numbers cause each one? Write them down.

### 4. Run and investigate: the fight (15 min)
1. Run it 10 times. Why is it different each time?
2. `import random` at the top loads a **library**, extra tools other programmers wrote for you. What happens if you delete that line?
3. What would `random.randint(1, 20)` do?

### 5. Modify together (15 min)
In `fight.py`, add an `and`:
```python
if roll == 6 and goblin_health > 5:
```
Talk about it: when is this true? Then try `or` instead.

## New words

| Word | Meaning |
|---|---|
| `<  >  <=  >=` | Less than, more than, less **or** same, more **or** same. |
| **`and`** | True only if **both** sides are true. |
| **`or`** | True if **at least one** side is true. |
| **`not`** | Flips it: `not True` is `False`. |
| **`True` / `False`** | The two answers to a yes/no question. Called **booleans**. |
| **`import`** | Load a library so you can use its tools. |
| **`random.randint(a, b)`** | A random whole number from a to b. |

---

## Mentor notes
- The shop fix is the payoff from quest 3.1 (buying 10 potions went negative). Point that out: he spotted a real bug two weeks ago and now he can fix it.
- **Ready check:** *Write an `if` that uses `and` or `or`, and explain when it's true. Use `random.randint` from a blank file.*
