# Week 5 · More Decisions — This week, on your own

**Get there:** from the main folder, type `cd weeks/05-more-decisions`

**Save as you go:** after each quest, commit it: `git add -A`, then `git commit -m "5.2 what you did"` with the quest number. See [GIT.md](../../GIT.md).

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 5.1 🔧 Shield for sale
In `shop2.py`, ask first: `"Potion or shield? "`. A shield costs 20 gold, but you can only buy one.
Use `if` / `else` to handle each item, and don't let the player go below 0 gold.
- [ ] Done

### 5.2 🔧 Fumble
In `fight.py`, rolling a **1** should be a fumble: your sword flies out of your hand. Add it so a 1 gets its own message, different from a 2.
- [ ] Done

### 5.3 🔮 Luck test
Run `fight.py` 20 times. Keep a tally in your notebook: how many crits, hits, misses and fumbles?
Do the numbers make sense for a 6-sided dice?
- [ ] Done

### 5.4 🧩 True or false?
Open `truth.py`. **Before running it**, write True or False for every `print` line on paper.
Then run it and count your mistakes. For each one you got wrong, figure out why.
The answer to check: **how many lines print `True`?**
- [ ] Done

### 5.5 🛠️ The castle guard
New blank file: `guard.py`. A guard won't let just anyone in. Ask the player:
- their name
- the password
- how much gold they have

The guard lets them in if they know the password **or** if they have more than 50 gold (a bribe).
But nobody named "Gerald" gets in, ever. (Gerald knows what he did.)
- [ ] Done

---

### ⭐ Stretch
- Make `fight.py` roll **two** dice and add them together. What's the most common total if you run it lots of times? Why?

---

## 📬 Hand it in
Before your next evening: `git push`, then open a pull request on GitHub (step 3 in [GIT.md](../../GIT.md)).
Your mentor reviews it, and you merge it together at your next evening.
