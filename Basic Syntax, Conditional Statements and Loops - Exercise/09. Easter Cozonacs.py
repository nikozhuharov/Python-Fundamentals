budget = float(input())
flour_price = float(input())
egg_price = 0.75*flour_price
milk_price = (1.25*flour_price)/4
cozonac_price = flour_price + egg_price + milk_price
cozonacs = 0
colored_eggs = 0
budget -= cozonac_price

while budget > 0:
    cozonacs += 1
    colored_eggs += 3
    if cozonacs % 3 == 0:
        colored_eggs -= cozonacs -2
    budget -= cozonac_price

budget += cozonac_price

print(f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")