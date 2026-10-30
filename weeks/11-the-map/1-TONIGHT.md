# Week 11 · The Map — Tonight's lesson

**Get there:** from the main folder, type `cd weeks/11-the-map`

**Start the week:** merge last week's pull request together, then `git checkout main`, `git pull`, `git checkout -b week-11`

**Together with your mentor, about 75 minutes.** You drive the keyboard.

## Tonight's idea

Tonight you put **everything** together: a dictionary of rooms, where each room is a dictionary, inside a `while` loop, with `if`s deciding where you go.
That's exactly how the week 1 dungeon works. By the end of tonight you'll be able to read it.

## Steps

### 1. Play (5 min)
Run `map.py`. Walk everywhere. Type `quit` when done.

### 2. Draw it (10 min)
On paper, draw the map: a box for each room, lines for the exits. Label each line with its direction.

### 3. Investigate (25 min)
This one line does a lot:
```python
room = rooms[room]["exits"][direction]
```
Work through it piece by piece, as if `room` is `"courtyard"` and `direction` is `"east"`:
1. What is `rooms["courtyard"]`?
2. What is `rooms["courtyard"]["exits"]`?
3. What is `rooms["courtyard"]["exits"]["east"]`?
4. So what does `room` become?

Then:
5. What's the job of the variable `room`? (It's the "you are here" marker.)
6. What does `list(rooms[room]["exits"])` show?
7. What happens if you type `north` at the gate twice in a row? Follow the code.

### 4. Modify together (15 min)
Add a new room: a **dungeon** below the tower, reached by `down` from `"tower"`.
Don't forget the way back `up`! Walk to it to test.

### 5. The big moment (15 min)
Open week 1's `dungeon.py`. Read it together from the top. Point at each part and say what it does.
Find: the rooms dict, the `room` variable, the inventory list, the game loop, the `break`s.
Anything still mysterious? Write it down. You'll learn `continue` and the rest soon.

## New words

| Word | Meaning |
|---|---|
| **nested** | Something inside something else: a dict inside a dict, an `if` inside a loop. |
| **state** | What the game remembers right now: which room, what you're carrying. |

---

## Mentor notes
- Step 5 is the payoff of the whole course so far. Make a moment of it. In week 1 this file was magic; now he can read it.
- If the nested lookup is confusing, add `print()` lines to show each piece, like `print(rooms[room])` and then `print(rooms[room]["exits"])`.
- **Ready check:** *Explain `rooms[room]["exits"][direction]` piece by piece, and add a new connected room to `map.py` without help.*
