n = int(input())
total = 0

for i in range(n):
    price_capsule = float(input())
    days = int(input())
    count_capsule = int(input())
    price = days * count_capsule * price_capsule
    print(f"The price for the coffee is: ${price:.2f}")
    total += price

print(f"Total: ${total:.2f}")