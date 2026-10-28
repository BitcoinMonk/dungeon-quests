# monster.py: a dictionary keeps a monster's stats together, each with a name

goblin = {"name": "Grubnik", "health": 15, "attack": 4}

print("A wild", goblin["name"], "appears!")
print("Health:", goblin["health"])
print("Attack:", goblin["attack"])

goblin["health"] = goblin["health"] - 6
print(goblin["name"], "takes 6 damage. Health is now", goblin["health"])

goblin["mood"] = "angry"
print(goblin)

for key in goblin:
    print(key, "->", goblin[key])
