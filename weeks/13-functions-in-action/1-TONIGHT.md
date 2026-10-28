# Week 13 · Functions in Action — Tonight's lesson

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

Functions aren't just for tiny jobs. They let you build a big program out of small pieces that each make sense on their own.
`battle_functions.py` is the battle from week 7, rebuilt out of functions. Now it can fight **two** monsters in a row without copying any code.

Next week you start your own dungeon, and this is how you'll keep it tidy.

## Steps

### 1. Predict (10 min)
Open `battle_functions.py`. Before running, find:
- Where does the program actually **start** doing things? (Not inside a `def`.)
- How many battles can happen? What decides whether the second one happens?

### 2. Run (5 min)
Play it two or three times.

### 3. Investigate (20 min)
1. `make_monster` is used for the hero too. Why does that work?
2. `attack(hero, goblin)` and `attack(goblin, hero)` are the same function. How does it know who's hitting who?
3. `attack` changes `defender["health"]`, and the change sticks after the function ends. Find where that matters.
4. `battle` **returns** `True` or `False`. Where is that used?
5. Compare with week 7's `battle.py`. Which is easier to add a third monster to?

### 4. Modify together (15 min)
Add a third battle against a monster of your choice. Then make the hero heal 10 health between battles.
How many lines did you need to add? (Not many. That's the point of functions.)

### 5. Look ahead (10 min)
Read `2-THIS-WEEK.md`, then quickly look at `../14-your-dungeon-design/` together, **just the title**. Next week, you start your own dungeon.
Start thinking: what's it about?

## New words

| Word | Meaning |
|---|---|
| **refactor** | Rewrite code so it's tidier, without changing what it does. |
| **`.split()`** | Chops a string into a list of words: `"fire 3".split()` is `["fire", "3"]`. You'll use it this week. |

---

## Mentor notes
- Point 3 (dictionaries changed inside a function stay changed) is subtle. You don't need to explain *why* yet, just that it works this way for lists and dicts.
- **Ready check:** *Add a new function to `battle_functions.py` from scratch (e.g. `heal(creature, amount)`) and use it.* Also: has he got an idea for his own dungeon? It's fine if it's rough.
