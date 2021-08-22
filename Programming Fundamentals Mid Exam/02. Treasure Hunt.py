treasure_chest = input().split("|")

command = input()
while command != "Yohoho!":
    command_list = command.split()
    if command_list[0] == "Loot":
        for i in range(1, len(command_list)):
            if command_list[i] not in treasure_chest:
                treasure_chest.insert(0, command_list[i])
    elif command_list[0] == "Drop":
        if 0 <= int(command_list[1]) < len(treasure_chest):
            treasure_chest.append(treasure_chest[int(command_list[1])])
            treasure_chest.remove(treasure_chest[int(command_list[1])])
    elif command_list[0] == "Steal":
        if len(treasure_chest) > int(command_list[1]):
            removed_list = treasure_chest[-int(command_list[1]):]
            print(", ".join(removed_list))
            treasure_chest = treasure_chest[:len(treasure_chest)-int(command_list[1])]
        else:
            print(", ".join(treasure_chest))
            treasure_chest.clear()
    command = input()

sum_items = 0

if treasure_chest:
    for item in treasure_chest:
        sum_items += len(item)
    print(f"Average treasure gain: {sum_items/len(treasure_chest):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")