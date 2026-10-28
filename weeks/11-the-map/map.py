# map.py: walk around a map made of a dictionary of dictionaries

rooms = {
    "gate": {
        "description": "A rusty castle gate. A courtyard lies to the north.",
        "exits": {"north": "courtyard"},
    },
    "courtyard": {
        "description": "An overgrown courtyard. Doors lead east and west. The gate is south.",
        "exits": {"south": "gate", "east": "stables", "west": "tower"},
    },
    "stables": {
        "description": "Empty stables. Something big left hoof prints here.",
        "exits": {"west": "courtyard"},
    },
    "tower": {
        "description": "The bottom of a tall tower. Stairs go up.",
        "exits": {"east": "courtyard", "up": "tower top"},
    },
    "tower top": {
        "description": "Wind howls. You can see the whole kingdom from here.",
        "exits": {"down": "tower"},
    },
}

room = "gate"

while True:
    print()
    print(rooms[room]["description"])
    print("Exits:", list(rooms[room]["exits"]))

    direction = input("> ").lower()

    if direction == "quit":
        break

    if direction in rooms[room]["exits"]:
        room = rooms[room]["exits"][direction]
    else:
        print("You can't go that way.")
