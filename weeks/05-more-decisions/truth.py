# truth.py: predict every line (True or False) BEFORE you run this file.

level = 7
has_key = False
is_wizard = True
gold = 15

print(level > 5 and has_key)
print(level > 5 or has_key)
print(is_wizard and gold > 10)
print(not has_key)
print(level == 7 and gold == 15 and is_wizard)
print(has_key or gold < 10)
print(not is_wizard or level < 10)
print((level > 10 or gold > 10) and not has_key)
print(level * 2 > gold and gold > 20)
print(is_wizard and not (level < 5 or has_key))
