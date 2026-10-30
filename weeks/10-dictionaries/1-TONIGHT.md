# Week 10 · Dictionaries — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/10-dictionaries`

**Start the week:** merge last week's pull request together, then `git checkout master`, `git pull`, `git checkout -b week-10`

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

A list finds things by **position** (0, 1, 2…). A **dictionary** finds things by **name**.
```python
goblin = {"name": "Grubnik", "health": 15, "attack": 4}
goblin["health"]     # 15
```
Each name (`"health"`) is a **key**, and what it points to (`15`) is its **value**. Like a real dictionary: look up a word, get its meaning.

## Steps

### 1. Predict (10 min)
Open `monster.py`. Don't run it. Write down what each `print` will show. The last loop is the trickiest.

### 2. Run (5 min)
Check your predictions.

### 3. Investigate (15 min)
1. What happens with `goblin["speed"]`, a key that doesn't exist? Read the error (`KeyError`).
2. How did `"mood"` get into the dictionary? There's no `append`.
3. In the `for` loop, is `key` the name (`"health"`) or the value (`15`)?
4. How is `goblin["health"] = goblin["health"] - 6` like `gold = gold - 6` from week 2?

### 4. Run and investigate: prices (10 min)
Open `prices.py`. Buy something, then try to buy a sword.
- How does it know what things cost?
- What does `if wanted in prices:` check: the keys or the values?

### 5. Modify together (15 min)
1. Add a `"sword": 25` to the shop. Run it. Did the menu update by itself? Why?
2. Make a second monster dictionary in `monster.py` for a dragon, and print both monsters' names and health.

## New words

| Word | Meaning |
|---|---|
| **dictionary** | Values you look up by name: `{"health": 15}`. Also called a **dict**. |
| **key** | The name you look up, like `"health"`. |
| **value** | What the key points to, like `15`. |
| **`d[key]`** | Get the value for a key. |
| **`d[key] = x`** | Change it, or add a new key. |
| **`KeyError`** | You asked for a key that isn't there. |

---

## Mentor notes
- Lists vs dicts is the key thing tonight. A good question to ask: "If you wanted the goblin's health, would you rather say `goblin[1]` or `goblin["health"]`?"
- Next week's map is a **dictionary of dictionaries**, so make sure single dicts feel easy first.
- **Ready check:** *From a blank file, make a dictionary for a hero with three stats, change one, add a new one, and print them all with a `for` loop.*
