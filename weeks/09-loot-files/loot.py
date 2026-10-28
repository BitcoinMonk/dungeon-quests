# loot.py: read the dragon's hoard from a file, one item per line

lines = open("loot.txt").read().splitlines()

print("The hoard has", len(lines), "things in it.")
print("The first five are:")

for thing in lines[:5]:
    print("-", thing)
