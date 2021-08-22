items = input().split("|")
budget = int(input())
profit = 0
revenue = 0

for item in items:
    products = item.split("->")
    name = products[0]
    price = float(products[1])
    if (name == "Clothes" and price <= 50) or (name == "Shoes" and price <= 35) or (name == "Accessories" and price <= 20.5):
        if budget >= price:
            budget -= price
            print(f"{price*1.4:.2f}", end=" ")
            profit += price*0.4
            revenue += price*1.4
print()
print(f"Profit: {profit:.2f}")
budget += revenue
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
