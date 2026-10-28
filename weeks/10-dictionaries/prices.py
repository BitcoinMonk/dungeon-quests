# prices.py: a shop that looks prices up in a dictionary

prices = {"potion": 7, "shield": 20, "rope": 3, "torch": 2}
gold = 30

print("For sale:")
for item in prices:
    print(f"  {item}: {prices[item]} gold")

wanted = input("What do you want to buy? ").lower()

if wanted in prices:
    cost = prices[wanted]
    if cost <= gold:
        gold = gold - cost
        print(f"You bought a {wanted}. You have {gold} gold left.")
    else:
        print("You can't afford that.")
else:
    print("We don't sell that here.")
