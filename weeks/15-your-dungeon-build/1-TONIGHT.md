# Week 15 · Your Dungeon: Build — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/14-your-dungeon-design`

**Start the week:** merge last week's pull request together, then `git checkout master`, `git pull`, `git checkout -b week-15`

**Together with your mentor, about 90 minutes.** You drive the keyboard.

## Tonight's idea

Your dungeon can be walked. Tonight it gets **danger**: a locked door and a monster.
Keep working in `weeks/14-your-dungeon-design/my_dungeon.py`. Don't copy it here; one file is easier.

## Steps

### 1. Show and tell (10 min)
Play your game for your mentor. Show them your bug list from 14.5.

### 2. The locked door (30 min)
Plan it out loud first:
- Which exit is locked?
- What item opens it?
- Where in the code do you check? (Hint: **before** you change `room`.)

Then build it. Test it **both ways**: without the item (door stays shut) and with it (door opens).

### 3. The monster (40 min)
Plan first:
- Is the monster a dictionary? (It probably should be.)
- Does it fight automatically when you enter the room, or do you type `fight`?
- What happens when it's defeated? Can it come back?

Use your functions from week 12's `toolbox.py` or week 13's `battle_functions.py`. Copy them into your file and change them to fit.

### 4. Look ahead (10 min)
Read `2-THIS-WEEK.md`. Next week is **launch night**.

---

## Mentor notes
- When he's stuck, ask "what does the game need to remember?" (usually the answer is a new variable) and "where in the loop should this check happen?"
- Resist fixing it for him. A slow fix he makes beats a fast one you make.
- **Ready check:** *The lock and the monster work, and the game can be won and lost.* If not, give it another week. Launch night waits for the game, not the calendar.
