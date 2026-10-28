# dice.py: functions are little machines you build once and use again and again

import random


def roll(sides):
    return random.randint(1, sides)


def announce(name, damage):
    print(f"{name} attacks for {damage} damage!")


def ask(question, options):
    while True:
        answer = input(f"{question} ({'/'.join(options)}) ").lower()
        if answer in options:
            return answer
        print("Please pick one of:", options)


announce("The hero", roll(6))
announce("The goblin", roll(4))

weapon = ask("Pick a weapon", ["sword", "bow", "spoon"])
print("You picked the", weapon)
