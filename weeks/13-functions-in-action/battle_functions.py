# battle_functions.py: week 7's battle, rebuilt out of functions

import random


def make_monster(name, health, attack):
    return {"name": name, "health": health, "attack": attack}


def attack(attacker, defender):
    damage = random.randint(1, attacker["attack"])
    defender["health"] = defender["health"] - damage
    print(f"{attacker['name']} hits {defender['name']} for {damage}. "
          f"{defender['name']} has {defender['health']} health left.")


def is_dead(creature):
    return creature["health"] <= 0


def battle(hero, monster):
    print(f"A {monster['name']} attacks!")
    while True:
        input("Press Enter to attack...")
        attack(hero, monster)
        if is_dead(monster):
            print(f"The {monster['name']} is defeated!")
            return True

        attack(monster, hero)
        if is_dead(hero):
            print("You have been defeated...")
            return False


hero = make_monster("Hero", 30, 6)
goblin = make_monster("Goblin", 12, 4)
troll = make_monster("Troll", 20, 5)

if battle(hero, goblin):
    print("You catch your breath... but something big is coming.")
    if battle(hero, troll):
        print("*** You cleared the cave! ***")
