# maze.py: an old map of the caves, and the directions scrawled on the back.
# Write your code at the bottom.

maze = {
    "start": {"south": "crooked stairs"},
    "rat palace": {"east": "glowing pond", "south": "flooded room"},
    "glowing pond": {"east": "chain room", "west": "rat palace"},
    "chain room": {"east": "spider nest", "south": "broken bridge", "west": "glowing pond"},
    "spider nest": {"west": "chain room"},
    "crooked stairs": {"north": "start", "south": "echo chamber"},
    "flooded room": {"east": "dripping cave", "north": "rat palace"},
    "dripping cave": {"south": "mossy tunnel", "west": "flooded room"},
    "broken bridge": {"east": "old well", "north": "chain room", "south": "mushroom grove"},
    "old well": {"south": "statue garden", "west": "broken bridge"},
    "echo chamber": {"north": "crooked stairs", "south": "goblin kitchen"},
    "bone pit": {"east": "mossy tunnel", "south": "lava vent"},
    "mossy tunnel": {"north": "dripping cave", "south": "crystal hall", "west": "bone pit"},
    "mushroom grove": {"north": "broken bridge", "south": "smelly den"},
    "statue garden": {"north": "old well", "south": "dusty crypt"},
    "goblin kitchen": {"east": "lava vent", "north": "echo chamber", "south": "frozen pool"},
    "lava vent": {"north": "bone pit", "south": "bat roost", "west": "goblin kitchen"},
    "crystal hall": {"east": "smelly den", "north": "mossy tunnel"},
    "smelly den": {"east": "dusty crypt", "north": "mushroom grove", "west": "crystal hall"},
    "dusty crypt": {"north": "statue garden", "south": "silent chapel", "west": "smelly den"},
    "frozen pool": {"east": "bat roost", "north": "goblin kitchen"},
    "bat roost": {"north": "lava vent", "west": "frozen pool"},
    "vault": {"east": "map room"},
    "map room": {"east": "silent chapel", "west": "vault"},
    "silent chapel": {"north": "dusty crypt", "west": "map room"},
}

directions = [
    "south", "south", "south", "south", "east", "north",
    "west", "south", "east", "north", "west", "south",
    "east", "north", "west", "north", "north", "north",
    "south", "south", "south", "south", "east", "north",
    "west", "north", "north", "north", "south", "south",
    "south", "east", "south", "west", "north", "north",
    "north", "north", "south", "south", "south", "south",
    "east", "north", "north", "east", "south", "east",
    "north", "north", "north", "east", "west", "south",
    "east", "south", "south", "west", "west", "north",
]

# Your code goes below this line.
