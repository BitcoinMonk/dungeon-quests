# Week 2 · Variables — This week, on your own

Do these in order. One or two a day. Change `[ ]` to `[x]` when a quest is done.

---

### 2.1 🔧 Your hero
In `hero.py`, change the hero's name, starting health and starting gold.
**Predict** the final gold and health on paper before you run it.
- [ ] Done

### 2.2 🔧 Potions
Add a variable `potions = 0`. Later in the story the hero finds 2 potions. Make `potions` go up by 2 and print it.
- [ ] Done

### 2.3 🔧 Drink one
At the end of `hero.py`, the hero drinks a potion: `health` goes up by 5 and `potions` goes down by 1. Print both.
- [ ] Done

### 2.4 🔮 Tricky predictions
Make a new file `predict.py` in this folder (right-click the folder in VS Code → **New File**). Type this in, but **predict each line on paper first**:
```python
a = 3
b = a + 2
a = 10
print(a, b)
print("a" + "b")
print("ha" * 3)
print("=" * 20)
```
Which ones surprised you? Write down why.
- [ ] Done

### 2.5 🧩 The dragon
The dragon has 1000 health. Your sword does 23 damage. Your fireball does 41 damage.
You hit it with the sword 17 times and with the fireball 9 times.
How much health does the dragon have left?
**Use Python**, not a calculator: make a file `dragon.py` with variables like `dragon_health`, `sword`, `fireball`. Check your answer with `check.py`.
- [ ] Done

### 2.6 🛠️ Hero card
New blank file: `hero_card.py`. Make variables for your own hero (name, class, health, strength, gold) and print a hero card that looks like this:
```
====================
  SIR NIBBLES
  Class: Knight
  Health: 30
  Strength: 7
  Gold: 12
====================
```
Bonus: work out a variable `power = health + strength * 2` and print it too.
- [ ] Done

---

### ⭐ Stretch
- What does `print(7 / 2)` show? What about `print(7 // 2)` and `print(7 % 2)`? Try to work out what `//` and `%` do. (You'll use them next week.)
