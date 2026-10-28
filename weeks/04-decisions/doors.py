# doors.py: choose a door

print("You stand before two doors: one red, one blue.")
choice = input("Which door? (red/blue) ")

if choice == "red":
    print("A wave of fire! You leap back just in time.")
elif choice == "blue":
    print("A quiet room with a chest full of gold.")
else:
    print("You stand there doing nothing. A bat poops on you.")

print("The adventure continues...")
