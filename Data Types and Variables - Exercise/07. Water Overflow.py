n = int(input())
capacity = 255
for i in range(n):
    liters = int(input())
    if liters <= capacity:
        capacity -= liters
    else:
        print("Insufficient capacity!")
print(255-capacity)

