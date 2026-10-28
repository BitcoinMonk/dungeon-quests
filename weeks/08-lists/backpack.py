# backpack.py: a list holds lots of things in one variable

backpack = ["torch", "rope", "bread"]

print("You are carrying:", backpack)
print("That's", len(backpack), "things.")
print("The first thing is the", backpack[0])

backpack.append("sword")
print("You found a sword! Now you have:", backpack)

backpack.remove("bread")
print("You ate the bread. Now you have:", backpack)

if "rope" in backpack:
    print("You tie the rope to a rock and climb down the well.")

print("Your backpack:")
for thing in backpack:
    print("-", thing)
