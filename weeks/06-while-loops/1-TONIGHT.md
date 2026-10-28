# Week 6 · While Loops — Tonight's lesson

**Together with your mentor, about 60 minutes.** You drive the keyboard.

## Tonight's idea

A **loop** runs the same lines again and again.
`while` keeps going **as long as** something is true. This is how every game keeps running: the week 1 dungeon is one big `while True:` loop.

## Steps

### 1. Predict (10 min)
Open `countdown.py`. Don't run it. Write down **every line** it will print.
Trace it like the computer: keep a note of what `seconds` is each time around.

### 2. Run (5 min)
Were you right? How many times did the loop run?

### 3. Investigate: countdown (10 min)
1. What happens if you delete `seconds = seconds - 1`? **Predict first.**
   (When it goes forever, click in the terminal and press **Ctrl+C** to stop it. Remember this trick.)
2. What do you change to count down from 10? From 100?
3. Why does "CRUNCH" only print once?

### 4. Play and investigate: guess (20 min)
1. Play `guess.py` twice.
2. `while True:` would loop forever. What makes it stop? Find the line.
3. What does `guesses = guesses + 1` do each time around?
4. Open week 1's `dungeon.py` and find its `while True:` and its `break`s. You can read part of it now!

### 5. Modify together (10 min)
Make `guess.py` print a hint when the guess is really close:
if the difference is 2 or less, print "You're very close!". (Hint: you might need to check both sides.)

## New words

| Word | Meaning |
|---|---|
| **loop** | Lines that run over and over. |
| **`while`** | Keep looping as long as this is true. |
| **`while True`** | Loop forever, until something says `break`. |
| **`break`** | Jump out of the loop right now. |
| **infinite loop** | A loop that never stops. **Ctrl+C** in the terminal stops it. |
| **counter** | A variable that goes up by 1 each time, like `guesses`. |

---

## Mentor notes
- Make sure he causes an infinite loop and stops it with Ctrl+C tonight. It's scary the first time and harmless after that.
- Tracing a loop on paper (writing the variable's value each time around) is the most useful skill this week. Do it out loud with him.
- **Ready check:** *From a blank file, write a loop that keeps asking a question until the player types `quit`.*
