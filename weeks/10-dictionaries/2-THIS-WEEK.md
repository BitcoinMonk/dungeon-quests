# Week 10 · Dictionaries — This week, on your own

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 10.1 🔧 Shopping spree
Change `prices.py` so you can keep buying things in a loop until you type `leave`. Keep track of your gold the whole time.
- [ ] Done

### 10.2 🔧 Fight a dictionary
Copy `battle.py` from week 7 into this folder. Change it so the goblin is a dictionary (`name`, `health`, `attack`) and the hero is too.
The fight should use `goblin["health"]` instead of `goblin_health`.
- [ ] Done

### 10.3 🔮 Dictionary puzzles
Make `dict_predict.py` and **predict** each line before running:
```python
hero = {"name": "Pip", "level": 3, "gold": 10}
print(hero["level"] + hero["gold"])
hero["gold"] = hero["gold"] * 2
print(hero["gold"])
print("name" in hero)
print("Pip" in hero)
print(len(hero))
```
Why is `"Pip" in hero` the answer it is?
- [ ] Done

### 10.4 🧩 The bestiary
Open `bestiary.py`. It's a dictionary of dictionaries: every monster's name points to its own stats.
To get the ogre's health you write `bestiary["ogre"]["health"]`. Try it.
**What is the total health of every monster in the bestiary?** Write your code at the bottom and check your answer.
- [ ] Done

### 10.5 🧩 Most dangerous
Still in `bestiary.py`: **which monster has the highest attack?** The answer is the monster's name.
Hint: keep two variables as you loop, the best attack so far and the name that had it. Check your answer.
- [ ] Done

### 10.6 🛠️ Your own bestiary
New blank file: `my_bestiary.py`. Invent 3 monsters as a dictionary of dictionaries, each with at least 3 stats.
Loop over it and print a card for each monster. You'll use these monsters in your own dungeon in week 14!
- [ ] Done

---

### ⭐ Stretch
- In `bestiary.py`: which monsters have more health than the average? Print their names.
