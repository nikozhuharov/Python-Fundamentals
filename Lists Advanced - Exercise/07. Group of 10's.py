numbers = input().split(", ")
numbers_int = [int(x) for x in numbers]
d = 0
collection = []

while numbers_int:
    collection.clear()
    d += 10
    for i in numbers_int:
        if i <= d:
            collection.append(i)
    for j in collection:
        numbers_int.remove(j)

    print(f"Group of {d}'s: {collection}")
