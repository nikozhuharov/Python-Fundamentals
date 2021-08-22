stops = input()
command = input()
while not command == "Travel":
    command_arg = command.split(":")
    if command_arg[0] == "Add Stop":
        index = int(command_arg[1])
        string = command_arg[2]
        if -len(stops) < index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif command_arg[0] == "Remove Stop":
        start_index = int(command_arg[1])
        end_index = int(command_arg[2])
        if -len(stops) <= start_index < len(stops) and -len(stops) <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]
        print(stops)
    elif command_arg[0] == "Switch":
        old_string = command_arg[1]
        new_string = command_arg[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")


