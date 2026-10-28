# shop.py: a tiny potion shop

gold = 30
price = 7

print("Welcome to the shop! You have", gold, "gold.")
print("Potions cost", price, "gold each.")

how_many = input("How many potions do you want? ")
how_many = int(how_many)

cost = how_many * price
gold = gold - cost

print(f"That's {cost} gold. You have {gold} gold left.")
