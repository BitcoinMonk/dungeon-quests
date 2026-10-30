# For the mentor

Everything you need is already in the repo. Each week's `1-TONIGHT.md` is the lesson plan, with **Mentor notes** at the bottom: what to watch for, and the **ready check**.

## Once, before week 2

He needs a GitHub account. On GitHub, open the repo's **Settings → Collaborators → Add people** and add his username so he can push branches. He accepts the invite from his email.
A ruleset on `master` (**Settings → Rules**) means his work only gets in through a PR you approve. You're the admin, so you can still push course updates straight to `master`.

## Each week on GitHub

He hands in each week as a **pull request** (branch `week-02` and so on; the routine is in [GIT.md](GIT.md)).
Before your evening, look over his PR on GitHub (**Files changed** tab) and leave a comment or two: one thing he did well, one question or fix. He answers by committing and pushing again.

## Every evening (about 90 minutes)

1. **Check in (15 min).** Open his pull request on GitHub together and go through **Files changed**. Run his 🛠️ Make quest. Go through anything he wrote down as stuck.
2. **Ready check (5 min).** Ask the ready check at the bottom of **last** week's `1-TONIGHT.md`.
   - **Pass:** approve the PR and have him click **Merge**. The merge is the sign-off.
   - **Not yet:** leave the PR open and repeat the week on the same branch. Redo the lesson with new examples and do the ⭐ stretch quests. This is normal, not failure.
3. **Start the new week (5 min).** The **Start the week** line at the top of the new `1-TONIGHT.md`: back to `master`, pull, new branch.
4. **Tonight's lesson (60 min).** Follow the new week's `1-TONIGHT.md`. **He drives the keyboard.**
5. **Look ahead (5 min).** Read the new `2-THIS-WEEK.md` together so he knows what's coming.

## How the lessons work

Every lesson follows **PRIMM**, a well-tested way to teach programming:

| Step | What happens |
|---|---|
| **Predict** | He reads code and says what it'll do, *before* running it. The most important step. Don't skip it. |
| **Run** | Run it and compare. Being wrong is where the learning is. |
| **Investigate** | Questions about how and why. Break it on purpose. |
| **Modify** | Change working code. |
| **Make** | Write something new from a blank file. Every week ends with one. |

## Pacing: how not to get ahead

- **Move on when the ready check passes, not when the calendar says.** 16 weeks is a guide. 20 is fine.
- **Ahead and bored?** Give him the ⭐ stretch quests or let him extend a Make quest. Don't skip weeks.
- **Behind?** Fewer quests is fine. 🧩 Puzzle and 🛠️ Make matter most; 🔧 Modify ones can be dropped.
- **Missed an evening?** Just carry on from where you left off.
- **The bonus week** (talking to a Minecraft server) fits any time after week 10, if he's itching for it.

## When he's stuck

Don't take the keyboard. Ask, in this order:
1. What did you expect to happen?
2. What actually happened?
3. What does the error say, and which line?
4. What could you `print` to see what's going on?

## AI

- **For him:** hints and explanations only, never "write this for me". It's rule 5 in the README.
- **For you:** paste any week's lesson into Claude to prep, or ask it to explain something you're unsure of.
- Every 🧩 puzzle has a worked solution in `mentor/solutions/puzzles.py`, using only what he knows by that week. From the main folder, run `python mentor/solutions/puzzles.py` to see all the answers.

## Homeschool

About 20–30 minutes a day, 4–5 days a week, is the right amount. His merged pull requests on GitHub are a dated record of everything he's done.

## Updating the course

If you change the course files, push them to `master`. He gets them with `git pull` when he starts the next week.
