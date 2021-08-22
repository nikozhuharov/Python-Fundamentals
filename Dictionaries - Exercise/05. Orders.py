products = {}

command = input()
while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name] = {"price": price, "quantity": quantity+products[name]["quantity"]}
    command = input()

for key, value in products.items():
    total_price = value["price"]*value["quantity"]
    print(f"{key} -> {total_price:.2f}")