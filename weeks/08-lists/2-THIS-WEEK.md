# Week 8 · Lists — This week, on your own

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 8.1 🔧 Pack for the trip
In `backpack.py`, add two new items, remove the torch, and print how many items are left using `len`.
- [ ] Done

### 8.2 🔮 List puzzles
Make `list_predict.py` and **predict** each line on paper before running:
```python
party = ["knight", "wizard", "thief", "cleric"]
print(party[1])
print(party[-1])
print(len(party))
print("thief" in party)
print("dragon" in party)
party.append("bard")
print(party[4])
```
- [ ] Done

### 8.3 🛠️ Pick it all up
New blank file: `pickup.py`. Start with an empty list: `inventory = []`.
Loop over and over, asking `"What do you pick up? (type done to stop) "`. Add each thing to the list.
When they type `done`, print everything they picked up, one per line, with numbers:
```
1. sword
2. old boot
3. cheese
```
Hint: you'll need a counter, or look up what `enumerate` does.
- [ ] Done

### 8.4 🧩 Big monsters
Open `horde.py`. It has a list of the health of every monster in a horde.
**How many monsters have more than 50 health?**
Write your code at the bottom of the file: loop over the list, and count with a variable. Check your answer.
- [ ] Done

### 8.5 🧩 The toughest one
Still in `horde.py`: what is the **highest** health in the horde?
Do it with a loop and a variable called `biggest`, not by reading the list with your eyes. Check your answer.
(Afterwards, try `print(max(horde))`. Python had a shortcut all along!)
- [ ] Done

---

### ⭐ Stretch
- In `horde.py`, what's the **total** health of the whole horde? What's the average?
- In `pickup.py`, don't let them pick up the same thing twice.
