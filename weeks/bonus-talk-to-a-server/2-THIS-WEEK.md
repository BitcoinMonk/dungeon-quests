# Bonus · Talk to a Server — On your own

**Get there:** from the main folder, type `cd weeks/bonus-talk-to-a-server`

**Save as you go:** after each quest, commit it: `git add -A`, then `git commit -m "B.1 what you did"` with the quest number. See [GIT.md](../../GIT.md).

Change `[ ]` to `[x]` when a quest is done.

---

### B.1 🔧 Server report
Make `server_status.py` print a nicer report: the server's message of the day, its version, and players online.
- [ ] Done

### B.2 🛠️ Server checker
New blank file: `checker.py`. Make a **list** of 3 or more Minecraft server addresses. Loop over them and print one line for each: online or offline, and how many players.
Use a function `check(server)` that returns the data dictionary.
- [ ] Done

### B.3 🛠️ Busiest server
Using your checker, find out which server in your list has the most players right now, and print its name.
- [ ] Done

---

### ⭐ Stretch
- Some servers also send back a list of player names (`data["players"]["list"]`), but only if they're small and allow it. Find one that does and print the names.

---

## 📬 Hand it in
Before your next evening: `git push`, then open a pull request on GitHub (step 3 in [GIT.md](../../GIT.md)).
Your mentor reviews it, and you merge it together at your next evening.
