# fight.py: one swing at a goblin, decided by a dice roll

import random

goblin_health = 10
roll = random.randint(1, 6)
print("You roll a", roll)

if roll == 6:
    print("CRITICAL HIT! The goblin explodes into glitter.")
elif roll >= 3:
    goblin_health = goblin_health - roll
    print(f"You hit! The goblin has {goblin_health} health left.")
else:
    print("You miss and trip over your own feet.")
