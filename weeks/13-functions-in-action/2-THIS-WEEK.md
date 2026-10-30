# Week 13 · Functions in Action — This week, on your own

**Get there:** from the main folder, type `cd weeks/13-functions-in-action`

**Save as you go:** after each quest, commit it: `git add -A`, then `git commit -m "13.2 what you did"` with the quest number. See [GIT.md](../../GIT.md).

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 13.1 🔧 Run away
In `battle_functions.py`, let the hero choose to `attack` or `run` each turn. Running has a 50% chance to work.
If it works, `battle` should return `True` (you survived).
- [ ] Done

### 13.2 🔮 Split it
Make `split_predict.py` and **predict** each line before running:
```python
line = "fire 7"
parts = line.split()
print(parts)
print(parts[0])
print(parts[1] + parts[1])
print(int(parts[1]) + int(parts[1]))
spell, level = line.split()
print(spell, level)
```
Why does `parts[1] + parts[1]` do what it does?
- [ ] Done

### 13.3 🛠️ Spell damage
`spells.txt` is the wizard's spell log: each line is a spell name and a level, like `fire 7`.
Make a blank file `spells.py` and write a function `damage(spell, level)` that returns how much damage a spell does:

| Spell | Damage |
|---|---|
| fire | level × 5 |
| ice | level × 3 + 2 |
| zap | level × level |
| heal | 0 (it doesn't hurt anyone) |

Test it: `damage("fire", 7)` should be 35, `damage("ice", 1)` should be 5, `damage("zap", 4)` should be 16.
- [ ] Done

### 13.4 🧩 Total damage
Using your `damage` function, read `spells.txt` (like week 9's loot) and work out the **total damage** of every spell in the log. Check your answer.
- [ ] Done

### 13.5 🧩 Big hits
**How many spells in the log do 50 or more damage?** Check your answer.
- [ ] Done

### 13.6 🛠️ Dungeon ideas
In your notebook (not code!), write down ideas for your own dungeon:
- What's the story? Why is the hero there?
- 5 to 8 room names.
- Items, monsters, and one locked door or puzzle.
- How do you win?
Bring it to your next evening.
- [ ] Done

---

### ⭐ Stretch
- Which **spell type** did the most damage in total across the whole log?

---

## 📬 Hand it in
Before your next evening: `git push`, then open a pull request on GitHub (step 3 in [GIT.md](../../GIT.md)).
Your mentor reviews it, and you merge it together at your next evening.
