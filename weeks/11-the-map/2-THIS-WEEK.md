# Week 11 · The Map — This week, on your own

**Get there:** from the main folder, type `cd weeks/11-the-map`

**Save as you go:** after each quest, commit it: `git add -A`, then `git commit -m "11.2 what you did"` with the quest number. See [GIT.md](../../GIT.md).

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 11.1 🔧 Grow the castle
Add **three** new rooms to `map.py`. Every room must be reachable, and you must be able to walk back. Update your paper map.
- [ ] Done

### 11.2 🔧 Things to find
Give each room in `map.py` an `"item"` (use `None` for rooms with nothing).
Add a `look` command that shows the item, and a `take` command that puts it in an `inventory` list and removes it from the room. Add an `inventory` command too.
Peek at week 1's `dungeon.py` if you get stuck. That's allowed, and real programmers do it all the time.
- [ ] Done

### 11.3 🔮 What's written in week 1?
In your notebook, write three things in week 1's `dungeon.py` that you understand now and didn't in week 1.
Then write one thing you still don't get. Bring it to your next evening.
- [ ] Done

### 11.4 🧩 Follow the old map
Open `maze.py`. It has a big map of caves (`maze`) and a list of `directions` someone scrawled on the back.
Start in `"start"` and follow every direction in order.
**Which room do you end up in?** The answer is the room name. Check it.
Hint: it's like `map.py`, but the directions come from the list instead of from `input`.
- [ ] Done

### 11.5 🧩 Rooms visited
Still in `maze.py`: following those directions, **how many different rooms did you visit**? Count `"start"` too, and count each room only once even if you go back to it.
Check your answer.
- [ ] Done

---

### ⭐ Stretch
- In `map.py`, make the tower top locked until you have an item from somewhere else.
- In `maze.py`, which room did you visit the **most** times?

---

## 📬 Hand it in
Before your next evening: `git push`, then open a pull request on GitHub (step 3 in [GIT.md](../../GIT.md)).
Your mentor reviews it, and you merge it together at your next evening.
