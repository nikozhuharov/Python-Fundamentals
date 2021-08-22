import re
products = []
total = 0
command = input()
pattern = r">>(?P<Product>[A-Za-z]+)<<(?P<Price>[0-9]+(\.[0-9]+)*)\!(?P<Quantity>[0-9]+)"
while command != "Purchase":
    text = re.finditer(pattern, command)
    for t in text:
        products.append(t.group("Product"))
        total += float(t.group("Price"))*int(t.group("Quantity"))
    command = input()

print("Bought furniture:")
for p in products:
    print(p)
print(f"Total money spend: {total:.2f}")