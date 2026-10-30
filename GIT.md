# Git: saving and handing in your work

**Git** keeps save points of your work, called **commits**. **GitHub** is where you hand it in, with a **pull request** (PR). Programmers everywhere work this way.

Every week goes on its own **branch** (`week-01`, `week-02`, …). You hand the week in as a pull request, your mentor reviews it, and at your next evening you merge it.

## Once, on your computer
```
git config --global user.name "Your Name"
git config --global user.email "the email on your GitHub account"
git config --global push.autoSetupRemote true
```

## Every week

### 1. Start the week (at your evening, after last week is merged)
```
git checkout master
git pull
git checkout -b week-02
```
Use the new week's number. `git pull` brings in last week's merged work and anything new your mentor added.

### 2. Every time you try something: commit
```
git status
git diff
git add -A
git commit -m "2.3 try: potion adds 10 health"
```
- `git status`: which files changed, and which branch you're on (first line).
- `git diff`: exactly what changed. Red is old, green is new. Press **q** to get out.
- Start the message with the quest number and say what you tried. If it didn't work, say so: `"2.3 try: health went down instead??"`.

**Commit broken code too.** Every attempt, not just the one that worked. Your mentor learns the most from the tries that didn't work, and you never lose anything.

### 3. End of every session: push
```
git push
```
The first push may open a browser to sign in to GitHub.
**The first push of the week only:** open the repo on GitHub. A yellow bar says your branch had recent pushes: click **Compare & pull request**, give it a title like `Week 2`, and click **Create pull request**. After that, every push adds to the same pull request by itself.

### 4. Hand it in (before your next evening)
Push one last time, then write **ready** as a comment on your pull request.

Your mentor reviews it. If they leave comments, fix things, commit, and `git push` again.
**Don't merge it yourself.** You merge it together at your next evening, after the ready check.

## Oops
| Problem | Fix |
|---|---|
| I broke a file and want it back how it was at my last commit | `git restore dungeon.py` |
| What have I committed? | `git log --oneline` (press **q** to get out) |
| Which branch am I on? | `git status`, first line |
| `git pull` says my local changes would be overwritten | Commit them first, or ask your mentor. |
