text = input()
command = input()

while not command == "Done":
    command_arg = command.split()
    if command_arg[0] == "Change":
        char = command_arg[1]
        replacement = command_arg[2]
        text = text.replace(char, replacement)
        print(text)
    elif command_arg[0] == "Includes":
        other_string = command_arg[1]
        if other_string in text:
            print(True)
        else:
            print(False)
    elif command_arg[0] == "End":
        other_string = command_arg[1]
        if other_string == text[-len(other_string):]:
            print(True)
        else:
            print(False)
    elif command_arg[0] == "Uppercase":
        text = text.upper()
        print(text)
    elif command_arg[0] == "FindIndex":
        char = command_arg[1]
        print(text.index(char))
    elif command_arg[0] == "Cut":
        start_index = int(command_arg[1])
        length = int(command_arg[2])
        print(text[start_index:start_index+length])
    command = input()