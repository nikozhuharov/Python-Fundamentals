parts = input().split("|")
command = input()

while command != "Done":
    c = command.split()
    if c[0] == "Add":
        particle = c[1]
        index = int(c[2])
        if 0 <= index < len(parts):
            parts.insert(index, particle)
    elif c[0] == "Remove":
        index = int(c[1])
        if 0 <= index < len(parts):
            parts.pop(index)
    elif c[0] == "Check" and c[1] == "Even":
        for i in range(len(parts)):
            if i % 2 == 0:
                print(parts[i], end=" ")
        print()
    elif c[0] == "Check" and c[1] == "Odd":
        for i in range(len(parts)):
            if i % 2 != 0:
                print(parts[i], end=" ")
        print()
    command = input()

print(f"You crafted {''.join(parts)}!")
