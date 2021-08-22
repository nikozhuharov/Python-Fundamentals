n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": float(rarity), "rate": []}

command = input()
while not command == "Exhibition":
    command_arg = command.split()
    if command_arg[0] == "Rate:":
        if len(command_arg) != 4:
            print("error")
        else:
            plant = command_arg[1]
            rate = command_arg[3]
            if rate.isnumeric() and plant in plants:
                rate = float(command_arg[3])
                plants[plant]["rate"].append(rate)
            else:
                print("error")
    elif command_arg[0] == "Update:":
        if len(command_arg) != 4:
            print("error")
        else:
            plant = command_arg[1]
            new_rarity = command_arg[3]
            if new_rarity.isnumeric() and plant in plants:
                new_rarity = float(command_arg[3])
                plants[plant]["rarity"] = new_rarity
            else:
                print("error")
    elif command_arg[0] == "Reset:":
        if len(command_arg) != 2:
            print("error")
        else:
            plant = command_arg[1]
            if plant in plants:
                plants[plant]["rate"].clear()
            else:
                print("error")
    else:
        print("error")
    command = input()

for plant in plants:
    if plants[plant]["rate"]:
        plants[plant]["rate"] = sum(plants[plant]["rate"])/len(plants[plant]["rate"])
    else:
        plants[plant]["rate"] = 0
sorted_plants = dict(sorted(plants.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rate"])))
print("Plants for the exhibition:")
for plant in sorted_plants:
    print(f"- {plant}; Rarity: {int(sorted_plants[plant]['rarity'])}; Rating: {sorted_plants[plant]['rate']:.2f}")
