products = input().split("|")
command = input()

while command != "Shop!":
    c = command.split("%")
    if c[0] == "Important":
        if c[1] in products:
            products.remove(c[1])
        products.insert(0, c[1])
    elif c[0] == "Add":
        if c[1] in products:
            print("The product is already in the list.")
        else:
            products.append(c[1])
    elif c[0] == "Swap":
        if c[1] in products and c[2] in products:
            index_p1 = products.index(c[1])
            index_p2 = products.index(c[2])
            products[index_p1], products[index_p2] = products[index_p2], products[index_p1]
        elif c[1] not in products:
            print(f"Product {c[1]} missing!")
        elif c[2] not in products:
            print(f"Product {c[2]} missing!")
    elif c[0] == "Remove":
        if c[1] in products:
            products.remove(c[1])
        else:
            print(f"Product {c[1]} isn't in the list.")
    elif c[0] == "Reversed":
        products.reverse()
    command = input()

counter = 1
for p in products:
    print(f"{counter}. {p}")
    counter += 1

