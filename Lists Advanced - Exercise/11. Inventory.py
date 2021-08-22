inventory = input().split(', ')

command = input()
while command != 'Craft!':
    command = command.split(" - ")
    if command[0] == "Collect":
        if not command[1] in inventory:
            inventory.append(command[1])
    if command[0] == "Drop":
        if command[1] in inventory:
            inventory.remove(command[1])
    if command[0] == "Combine Items":
        items = command[1].split(':')
        if items[0] in inventory:
            inventory.insert(inventory.index(items[0]) + 1, items[1])
    if command[0] == "Renew":
        if command[1] in inventory:
            inventory.remove(command[1])
            inventory.append(command[1])
    command = input()

print(", ".join(inventory))

