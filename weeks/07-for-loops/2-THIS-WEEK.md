# Week 7 · For Loops — This week, on your own

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 7.1 🔧 Rocket launch
Make `launch.py`: count down from 10 to 1 with a `for` loop, then print `"LIFT OFF!"`.
- [ ] Done

### 7.2 🔧 Potion break
In `battle.py`, before each attack ask: `"attack or potion? "`.
A potion heals 6 health, but you only have **2**. If you're out, say so and lose the turn.
- [ ] Done

### 7.3 🔮 Loop the loop
Make `nested.py` and **predict** the output before running:
```python
for row in range(3):
    for col in range(4):
        print("#", end="")
    print()
```
(`end=""` means "don't start a new line after printing".) How many `#` in total? Why?
- [ ] Done

### 7.4 🧩 The golden staircase
A magic staircase has 100 steps. On step 1 you find 1 gold, on step 2 you find 2 gold, on step 3 you find 3 gold… all the way to step 100.
How much gold do you have at the top?
Write `golden_stairs.py` with a `for` loop and a `total` variable. Check your answer.
- [ ] Done

### 7.5 🧩 Goblin tower
A goblin tower has 50 floors. Floor 1 has 3 goblins. Every floor has **2 more** goblins than the floor below it (floor 2 has 5, floor 3 has 7…).
How many goblins are in the whole tower?
Write `goblin_tower.py`. Check your answer.
- [ ] Done

### 7.6 🛠️ Training montage
New blank file: `training.py`. Your hero trains for 10 days. Use a `for` loop over the days.
Each day, `strength` goes up by a random amount from 1 to 3. Print a line for each day like `Day 4: strength is now 9`, and a final message at the end.
- [ ] Done

---

### ⭐ Stretch
- Use the nested loop idea from 7.3 to draw a triangle:
  ```
  #
  ##
  ###
  ####
  ```
