lost = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
i = 0
total = 0
broken_shield = 0

while lost > 0:
    i += 1
    if i % 2 == 0:
        total += helmet_price
    if i % 3 == 0:
        total += sword_price
        if i % 2 == 0:
            total += shield_price
            broken_shield += 1
            if broken_shield % 2 == 0:
                total += armor_price
    lost -= 1

print(f"Gladiator expenses: {total:.2f} aureus")
