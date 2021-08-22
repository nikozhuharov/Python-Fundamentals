gifts = input().split()
command = input()
while command != "No Money":
    command_list = command.split()
    if command_list[0] == "OutOfStock":
        gifts = ["None" if x == command_list[1] else x for x in gifts]
    elif command_list[0] == "Required":
        if 0 < int(command_list[2]) < len(gifts):
            gifts[int(command_list[2])] = command_list[1]
    elif command_list[0] == "JustInCase":
        gifts[-1] = command_list[1]
    command = input()

for i in range(len(gifts)):
    if gifts[i] != "None":
        print(str(gifts[i]), end=" ")
