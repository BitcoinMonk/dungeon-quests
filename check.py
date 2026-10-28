# check.py: check a puzzle answer. Press the play button and answer the two questions.
# The answers are scrambled (hashed) so you can't just read them here. Nice try, though.

import hashlib

ANSWERS = {
    "1.7": "e0aa6b9f50dd105d",
    "2.5": "4fd2b7d66d3a7ef6",
    "3.4": "252f11765c361278",
    "3.5": "41827b45f0d5f02f",
    "4.4": "cc4f16b22415c1bc",
    "5.4": "3c8da78848ac921d",
    "6.4": "be24bf738e3e2ec8",
    "6.5": "60a7583731e054cb",
    "7.4": "0540bddd02872111",
    "7.5": "15bc951bdfbde298",
    "8.4": "ca93bedd28ab5f58",
    "8.5": "99267c9bd7703ad8",
    "9.1": "ed54c02f9896f8f7",
    "9.2": "528b917f9e85ff0f",
    "9.3": "a56d77b5d8228707",
    "10.4": "0b70c1ab9102ff1f",
    "10.5": "3e41c4aee954d2b3",
    "11.4": "3266b1127e19427b",
    "11.5": "81303cf852a30fb0",
    "12.4": "f4db85eca9e31a2f",
    "13.4": "2fde83e7e0b39fc4",
    "13.5": "4e8547bf7073f845",
}


def fingerprint(quest, answer):
    cleaned = " ".join(answer.strip().lower().split())
    return hashlib.sha256(f"{quest}:{cleaned}".encode()).hexdigest()[:16]


quest = input("Which quest? (like 2.5) ").strip()

if quest not in ANSWERS:
    print("That quest doesn't have an answer to check. Only the puzzle quests do.")
else:
    answer = input("Your answer: ")
    if fingerprint(quest, answer) == ANSWERS[quest]:
        print()
        print("  *** CORRECT! ***")
        print("  Tick it off in 2-THIS-WEEK.md.")
    else:
        print()
        print("  Not quite. Check your code and try again.")
        print("  Tip: print your variables partway through to see what's happening.")
