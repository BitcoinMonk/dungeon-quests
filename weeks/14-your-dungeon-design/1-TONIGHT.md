# Week 14 · Your Dungeon: Design — Tonight's lesson

**Together with your mentor, about 90 minutes.** You drive the keyboard, and tonight you're also the boss.

## Tonight's idea

For three weeks you build **your own** dungeon game, from a **blank file**. Your mentor plays it on launch night (week 16).
Real programmers plan before they type. Tonight is half plan, half code.

You may look at any earlier week's code at any time. That's not cheating; it's how programming works.

## Steps

### 1. Design (30 min)
Open `DESIGN.md` and fill it in together, starting from your notes from quest 13.6.
Keep it small: **5 to 8 rooms**, one monster, one lock. You can add more later.
Then draw the map on paper.

### 2. Plan the order (10 min)
Big programs get built in small working steps. Here's the order you'll follow, one step at a time, running the game after **every** step:

1. Walk between rooms
2. `look`
3. Items and `take`
4. `inventory`
5. The locked door
6. The monster
7. Winning and losing
8. Your special thing

Steps 1–4 are this week. Steps 5–8 are next week.

### 3. Start building: step 1 (40 min)
Make a **blank** file in this folder: `my_dungeon.py`.
1. Type in your `rooms` dictionary from `DESIGN.md`: descriptions and exits only for now.
2. Add the `room` variable and the game loop so you can walk around.
3. Run it. Walk to every room. Does every exit go where your map says?

If you get stuck, look at how week 11's `map.py` did it, then close it and type your own.

## New words

| Word | Meaning |
|---|---|
| **design** | The plan for what you're building. |
| **milestone** | A small step where the program works, even if it's not finished. |
| **playtest** | Playing your own game to find bugs. |

---

## Mentor notes
- Scope is the danger tonight. He'll want 30 rooms and a dragon army. Cap it at 8 rooms and let him grow it after launch night.
- Let him own the decisions. Your job is asking "how will the code know that?", not designing it for him.
- **Ready check** (start of next evening): *His game walks between all rooms, and `look`, `take` and `inventory` work.* If not, that's fine: spend next evening finishing steps 1–4 and push launch night back a week.
