# Week 3 · Input and Math — This week, on your own

**Get there:** from the main folder, type `cd weeks/03-input-and-math`

**Save as you go:** commit every time you try something, even when it's broken: `git add -A`, then `git commit -m "3.2 try: what you changed"`. `git push` at the end of every session. See [GIT.md](../../GIT.md).

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 3.1 🔮 Bad customers
Run `shop.py` and type `three` (the word, not the number). Read the error and write in your notebook what you think it means.
Then try buying `10` potions. What's weird about the answer? (You'll fix it in week 5.)
- [ ] Done

### 3.2 🔧 Name your hero
Copy `hero.py` from week 2 into this folder. Change it so the hero's name comes from `input()` instead of being written in the code.
- [ ] Done

### 3.3 🔧 Better shop
In `shop.py`, add a second item: the player also gets asked how many **arrows** they want (2 gold each). Work out the total cost of potions plus arrows and print it in an f-string.
- [ ] Done

### 3.4 🧩 Sword sale
You have 250 gold. Swords cost 32 gold each. You buy as many swords as you can afford.
How much gold do you have left?
Write `swords.py` and use `//` and `%`. Check the answer with `check.py`.
- [ ] Done

### 3.5 🧩 The long walk
On a long road, you find a potion every 7 steps (at step 7, step 14, step 21…).
You walk 1000 steps. How many potions did you find?
Write `walk.py` to work it out, then check it.
- [ ] Done

### 3.6 🛠️ Character creator
New blank file: `creator.py`. Ask the player for:
- their hero's name
- their age

Then make up stats from the answers, like `health = age * 3` or `luck = age % 7`, and print a hero card with f-strings.
- [ ] Done

---

### ⭐ Stretch
- What does `input()` give you if the player just presses Enter without typing anything? Find out.
- Add a "discount": if the player buys potions, they get 3 gold back. Print the final gold.

---

## 📬 Hand it in
Done with the week? `git push`, then write **ready** as a comment on your pull request (step 4 in [GIT.md](../../GIT.md)).
Your mentor reviews it, and you merge it together at your next evening.
