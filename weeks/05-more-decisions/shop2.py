# shop2.py: the shop from week 3, but it won't let you go broke

gold = 30
price = 7

print("You have", gold, "gold. Potions cost", price, "each.")
how_many = int(input("How many potions? "))
cost = how_many * price

if cost <= gold:
    gold = gold - cost
    print(f"Here you go! You have {gold} gold left.")
else:
    print(f"You can't afford that. It costs {cost} but you only have {gold}.")
