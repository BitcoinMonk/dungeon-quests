# Week 1 · The Dungeon — This week, on your own

**Get there:** from the main folder, type `cd weeks/01-the-dungeon`

**Save as you go:** commit every time you try something, even when it's broken: `git add -A`, then `git commit -m "1.2 try: what you changed"`. `git push` at the end of every session. See [GIT.md](../../GIT.md).

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.
Everything this week happens in `dungeon.py`.

---

### 1.1 🎮 Beat the game
Win the game. If the goblin eats you, read the room descriptions more carefully. They're hints.
- [ ] Done

### 1.2 🔮 Predict the inventory
Start a new game. Pick up the sword, then type `inventory`.
**Before you press Enter**, write in your notebook exactly what you think it will print. Were you right? What were the square brackets `[ ]`?
- [ ] Done

### 1.3 🔧 Make it your game
Change the title `DUNGEON QUEST` to your own game name. Change the "You wake up…" story line to your own beginning.
- [ ] Done

### 1.4 🔧 Spooky library
Rewrite the library's description so it's creepy. Then change one more room description.
- [ ] Done

### 1.5 🔧 New monster
Change the goblin into a different monster. Use **Ctrl+F** (**Cmd+F** on Mac) to find every place that says "goblin" or "GOBLIN". Play the game to make sure your monster shows up everywhere.
- [ ] Done

### 1.6 🔧 Break it on purpose
Try each of these, one at a time. Run, read the error, write in your notebook what the last line said, then undo it.
1. Delete a `"` from a print line.
2. Delete the `:` at the end of `while True:`.
3. Change `print` to `prnt` somewhere.
- [ ] Done

### 1.7 🧩 The secret command
There's a secret command hidden in the code that isn't in the list the game shows you. Find it by **reading the code**, then use it in the game. It gives you a number.
Check your answer: from this week's folder, run `python ../../check.py`, then enter quest `1.7` and the number.
- [ ] Done

---

### ⭐ Stretch: build your own room (only if everything else is done)
1. **Copy a room.** At the top of `dungeon.py`, every room is a block that starts with its name, like `"library": {`, and ends with `},`. Copy the whole armory block and paste it right under itself.
2. **Make it yours.** Change the name (`"armory"` → something like `"kitchen"`) and write a new description.
3. **Connect it.** Rooms connect through their `"exits"`. Add an exit from the hallway to your room (the hallway has no `"down"` yet, so use that), and change your room's exits so `"up"` leads back to `"hallway"`. Watch the commas and quotes; copy the pattern you see.
4. **Walk there.** Run the game, go to the hallway, type `down`. If you get an error, read the line number it names.
5. **Put something in it.** Change your room's `"item"` to something new and pick it up with `take`.

Harder: make the hallway description hint that there's a way down.

---

## 📬 Hand it in
Done with the week? `git push`, then write **ready** as a comment on your pull request (step 4 in [GIT.md](../../GIT.md)).
Your mentor reviews it, and you merge it together at your next evening.
