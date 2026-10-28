# Week 6 · While Loops — This week, on your own

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 6.1 🔧 Harder wizard
Change `guess.py` so the number is from 1 to 100. Play it 3 times and write down how many guesses each game took.
What's the best way to guess? (Think about which number to guess **first**.)
- [ ] Done

### 6.2 🔧 Limited guesses
Change `guess.py` so you only get 7 guesses. If you run out, print `"The wizard laughs. It was ..."` with the secret number.
Hint: the loop could check `while guesses < 7:` instead of `while True:`. But then how do you know if they won or lost after the loop?
- [ ] Done

### 6.3 🔮 Loop puzzles
Make `trace.py`. For each loop, **predict on paper** what it prints, then run it:
```python
n = 1
while n < 50:
    n = n * 2
print(n)

x = 10
while x > 0:
    x = x - 3
print(x)
```
- [ ] Done

### 6.4 🧩 The slime
A slime splits in two every minute. It starts as **1** slime. After 1 minute there are 2, after 2 minutes there are 4, and so on.
After how many minutes are there **more than 1,000,000** slimes?
Write `slime.py` using a `while` loop and a counter for minutes. Check your answer.
- [ ] Done

### 6.5 🧩 The potion bank
You put 100 gold in the goblin bank. Each year, the goblins add 10% (so 100 becomes 110, then 121, and so on; use `gold = gold * 1.1`).
How many years until you have **at least 1000** gold?
Write `bank.py` to find out. Check your answer.
- [ ] Done

### 6.6 🛠️ Campfire menu
New blank file: `campfire.py`. The hero sits at a campfire. Show a menu over and over until they leave:
```
1. Rest (+5 health)
2. Eat (+2 health)
3. Check health
4. Leave camp
```
Keep a `health` variable. Health can't go above 30.
- [ ] Done

---

### ⭐ Stretch
- In `campfire.py`, add a 1-in-6 chance (use `random`) that a wolf attacks while you rest.
