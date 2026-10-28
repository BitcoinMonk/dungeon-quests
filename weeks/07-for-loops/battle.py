# battle.py: fight a goblin until one of you falls

import random

hero_health = 20
goblin_health = 15

while hero_health > 0 and goblin_health > 0:
    input("Press Enter to attack...")

    hit = random.randint(1, 6)
    goblin_health = goblin_health - hit
    print(f"You hit for {hit}. Goblin health: {goblin_health}")

    if goblin_health <= 0:
        break

    bite = random.randint(1, 4)
    hero_health = hero_health - bite
    print(f"The goblin bites for {bite}. Your health: {hero_health}")

if hero_health > 0:
    print("VICTORY!")
else:
    print("You have been defeated...")
