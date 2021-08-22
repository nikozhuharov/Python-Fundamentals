def valid(sequence, index):
    if 0 <= index < len(sequence):
        return True
    return False


def shoot(sequence, index, power):
    if valid(sequence, index):
        sequence[index] -= power
        if sequence[index] <= 0:
            sequence.pop(index)


def add(sequence, index, value):
    if valid(sequence, index):
        sequence.insert(index, value)
    else:
        print("Invalid placement!")


def strike(sequence, index, radius):
    if valid(sequence, index-radius) and valid(sequence, index+radius):
        del sequence[index-radius:index+radius+1]
    else:
        print("Strike missed!")


sequence = input().split()
sequence = [int(x) for x in sequence]

command = input()
while command != "End":
    command_list = command.split()
    if command_list[0] == "Shoot":
        index = int(command_list[1])
        power = int(command_list[2])
        shoot(sequence, index, power)
    elif command_list[0] == "Add":
        index = int(command_list[1])
        value = int(command_list[2])
        add(sequence, index, value)
    elif command_list[0] == "Strike":
        index = int(command_list[1])
        radius = int(command_list[2])
        strike(sequence, index, radius)
    command = input()

sequence = [str(x) for x in sequence]
print('|'.join(sequence))
