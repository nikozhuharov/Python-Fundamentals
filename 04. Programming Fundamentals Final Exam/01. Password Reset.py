password = input()
command = input()

while not command == "Done":
    command_arg = command.split()
    if command_arg[0] == "TakeOdd":
        new_password = ""
        for i in range(len(password)):
            if not i % 2 == 0:
                new_password += password[i]
        password = new_password
        print(password)
    elif command_arg[0] == "Cut":
        index = int(command_arg[1])
        length = int(command_arg[2])
        password = password[:index] + password[index+length:]
        print(password)
    elif command_arg[0] == "Substitute":
        substring = command_arg[1]
        substitute = command_arg[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")