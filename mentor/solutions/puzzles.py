# Reference solutions for every puzzle quest. Run it to print every answer.
# Student? This file is for your mentor. Close it now. Solving the puzzle yourself is the whole point.
# Written with only what he's learned by that week, so you can show him one way it could look.

from pathlib import Path

weeks = Path(__file__).parent.parent.parent / "weeks"


def week_1_7():
    return 37 * 12


def week_2_5():
    dragon_health = 1000
    sword = 23
    fireball = 41
    dragon_health = dragon_health - sword * 17
    dragon_health = dragon_health - fireball * 9
    return dragon_health


def week_3_4():
    gold = 250
    price = 32
    return gold % price


def week_3_5():
    return 1000 // 7


def week_4_4():
    # Try every candidate the riddle allows.
    for number in range(41, 50):
        if number % 2 == 0 and number % 4 != 0 and number != 42:
            return number


def week_5_4():
    level = 7
    has_key = False
    is_wizard = True
    gold = 15
    lines = [
        level > 5 and has_key,
        level > 5 or has_key,
        is_wizard and gold > 10,
        not has_key,
        level == 7 and gold == 15 and is_wizard,
        has_key or gold < 10,
        not is_wizard or level < 10,
        (level > 10 or gold > 10) and not has_key,
        level * 2 > gold and gold > 20,
        is_wizard and not (level < 5 or has_key),
    ]
    return lines.count(True)


def week_6_4():
    slimes = 1
    minutes = 0
    while slimes <= 1000000:
        slimes = slimes * 2
        minutes = minutes + 1
    return minutes


def week_6_5():
    gold = 100
    years = 0
    while gold < 1000:
        gold = gold * 1.1
        years = years + 1
    return years


def week_7_4():
    total = 0
    for step in range(1, 101):
        total = total + step
    return total


def week_7_5():
    total = 0
    goblins = 3
    for floor in range(50):
        total = total + goblins
        goblins = goblins + 2
    return total


def horde():
    source = (weeks / "08-lists" / "horde.py").read_text()
    scope = {}
    exec(source, scope)
    return scope["horde"]


def week_8_4():
    count = 0
    for health in horde():
        if health > 50:
            count = count + 1
    return count


def week_8_5():
    biggest = 0
    for health in horde():
        if health > biggest:
            biggest = health
    return biggest


def loot():
    return open(weeks / "09-loot-files" / "loot.txt").read().splitlines()


def week_9_1():
    return len(loot())


def week_9_2():
    count = 0
    for thing in loot():
        if thing == "gem":
            count = count + 1
    return count


def week_9_3():
    total = 0
    for thing in loot():
        if thing == "gold coin":
            total = total + 1
        elif thing == "gem":
            total = total + 25
        elif thing == "crown":
            total = total + 100
    return total


def bestiary():
    scope = {}
    exec((weeks / "10-dictionaries" / "bestiary.py").read_text(), scope)
    return scope["bestiary"]


def week_10_4():
    total = 0
    beasts = bestiary()
    for name in beasts:
        total = total + beasts[name]["health"]
    return total


def week_10_5():
    best_attack = 0
    best_name = ""
    beasts = bestiary()
    for name in beasts:
        if beasts[name]["attack"] > best_attack:
            best_attack = beasts[name]["attack"]
            best_name = name
    return best_name


def maze_walk():
    scope = {}
    exec((weeks / "11-the-map" / "maze.py").read_text(), scope)
    room = "start"
    visited = ["start"]
    for direction in scope["directions"]:
        room = scope["maze"][room][direction]
        if room not in visited:
            visited.append(room)
    return room, visited


def week_11_4():
    return maze_walk()[0]


def week_11_5():
    return len(maze_walk()[1])


def is_lucky(n):
    return n % 7 == 0 or n % 10 == 7


def week_12_4():
    count = 0
    for n in range(1, 1001):
        if is_lucky(n):
            count = count + 1
    return count


def damage(spell, level):
    if spell == "fire":
        return level * 5
    elif spell == "ice":
        return level * 3 + 2
    elif spell == "zap":
        return level * level
    return 0


def spell_damages():
    damages = []
    for line in open(weeks / "13-functions-in-action" / "spells.txt").read().splitlines():
        spell, level = line.split()
        damages.append(damage(spell, int(level)))
    return damages


def week_13_4():
    return sum(spell_damages())


def week_13_5():
    count = 0
    for d in spell_damages():
        if d >= 50:
            count = count + 1
    return count


if __name__ == "__main__":
    for name, func in list(globals().items()):
        if name.startswith("week_"):
            quest = name[5:].replace("_", ".")
            print(f"{quest}: {func()}")
