# Week 4 · Decisions — This week, on your own

**Get there:** from the main folder, type `cd weeks/04-decisions`

**Save as you go:** commit every time you try something, even when it's broken: `git add -A`, then `git commit -m "4.2 try: what you changed"`. `git push` at the end of every session. See [GIT.md](../../GIT.md).

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 4.1 🔧 Inside the blue door
In `doors.py`, when the player picks blue, ask another question: `"Open the chest? (yes/no) "`.
If yes, they find something. If no, something else happens.
You'll need an `if` *inside* an `if`. Watch your indentation: the inner one goes in further.
- [ ] Done

### 4.2 🔮 Number checks
Make `compare.py` and predict each line (True or False) on paper before running:
```python
print(5 > 3)
print(5 < 3)
print(5 == 5)
print(5 != 5)
print(10 >= 10)
print("cat" == "Cat")
```
`!=` means "is **not** the same". `>=` means "bigger than **or** the same".
- [ ] Done

### 4.3 🔧 The bridge troll
Make `troll.py`. A troll asks "How much gold will you pay to cross?" (use `input` and `int`).
- 10 or more: he lets you cross.
- 1 to 9: he laughs and takes the gold anyway.
- 0: he throws you in the river.
- [ ] Done

### 4.4 🧩 The number door
A door has a riddle carved on it:

> *I am a number bigger than 40 and smaller than 50.*
> *I am even. Divide me by 4 and something is left over.*
> *I am not 42, because that would be too obvious.*

Write `number_door.py`: ask for a number and use `if` checks to say whether the door opens. Then use it to find the number. (Hint: "even" means `number % 2 == 0`.)
Check the answer with `check.py`.
- [ ] Done

### 4.5 🛠️ Riddle game
New blank file: `riddle.py`. Ask the player a riddle. If they get it right, print a reward. If wrong, print what the answer was.
Make it accept the answer in capitals too.
- [ ] Done

---

### ⭐ Stretch
- Make `riddle.py` ask **three** riddles and keep a `score` variable. Print the score at the end.

---

## 📬 Hand it in
Done with the week? `git push`, then write **ready** as a comment on your pull request (step 4 in [GIT.md](../../GIT.md)).
Your mentor reviews it, and you merge it together at your next evening.
