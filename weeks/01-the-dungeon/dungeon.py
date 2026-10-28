# DUNGEON QUEST
# Press the play button (top right of VS Code) to run this game.
# You don't need to understand this code yet. By week 11 you'll be able to read all of it.

# The map: every room has a description, exits to other rooms, and maybe an item.
rooms = {
    "cell": {
        "description": "A damp stone cell. The door to the north hangs open.",
        "exits": {"north": "hallway"},
        "item": None,
    },
    "hallway": {
        "description": "A long hallway lit by flickering torches. You hear growling to the north.",
        "exits": {"south": "cell", "east": "armory", "west": "library", "north": "throne room"},
        "item": None,
    },
    "armory": {
        "description": "Racks of rusty weapons, mostly broken. One still looks sharp.",
        "exits": {"west": "hallway"},
        "item": "sword",
    },
    "library": {
        "description": "Dusty books from floor to ceiling. Something glints on a shelf.",
        "exits": {"east": "hallway"},
        "item": "key",
    },
    "throne room": {
        "description": "A huge room with a crumbling throne. Behind it, a locked door leads north.",
        "exits": {"south": "hallway", "north": "treasure room"},
        "item": None,
    },
    "treasure room": {
        "description": "Gold. Piles and piles of gold, as far as you can see.",
        "exits": {},
        "item": None,
    },
}

room = "cell"
inventory = []
monster_alive = True

print("==========================")
print("       DUNGEON QUEST")
print("==========================")
print("You wake up on a cold floor. Your head hurts.")
print("Commands: north, south, east, west, look, take, inventory, quit")
print()
print(rooms[room]["description"])

while True:
    command = input("> ").strip().lower()

    if command == "quit":
        print("You curl up on the floor and give up. Game over.")
        break

    elif command == "look":
        print(rooms[room]["description"])
        if rooms[room]["item"]:
            print("You see a", rooms[room]["item"], "here.")

    elif command == "take":
        item = rooms[room]["item"]
        if item:
            inventory.append(item)
            rooms[room]["item"] = None
            print("You pick up the", item + ".")
        else:
            print("There's nothing here to take.")

    elif command == "inventory":
        print("You are carrying:", inventory)

    elif command == "dig" and room == "cell":
        print("You scrape at the dirt floor and find an old coin.")
        print("It is stamped with the number", 37 * 12)

    elif command in rooms[room]["exits"]:
        next_room = rooms[room]["exits"][command]

        if next_room == "treasure room" and "key" not in inventory:
            print("The door is locked. You need a key.")
            continue

        room = next_room
        print(rooms[room]["description"])

        if room == "throne room" and monster_alive:
            print("A GOBLIN leaps off the throne!")
            if "sword" in inventory:
                print("You swing your sword. The goblin runs away screaming.")
                monster_alive = False
            else:
                print("You have nothing to fight with. The goblin eats you. GAME OVER.")
                break

        if room == "treasure room":
            print("*** YOU WIN! ***")
            break

    else:
        print("You can't do that here.")
