def exchange(index: int, input_list):
    return input_list[index+1:]+input_list[:index+1]


def find_index(element, input_list):
    for i in range(len(input_list)):
        if input_list[i] == element:
            index = i
    return index


def max_even_odd(filter, input_list):
    if filter == "even":
        even_list = [x for x in input_list if x % 2 == 0]
        if not even_list:
            return "No matches"
        else:
            return find_index(max(even_list), input_list)
    elif filter == "odd":
        odd_list = [x for x in input_list if x % 2 != 0]
        if not odd_list:
            return "No matches"
        else:
            return find_index(max(odd_list), input_list)


def min_even_odd(filter, input_list):
    if filter == "even":
        even_list = [x for x in input_list if x % 2 == 0]
        if not even_list:
            return "No matches"
        else:
            return find_index(min(even_list), input_list)
    elif filter == "odd":
        odd_list = [x for x in input_list if x % 2 != 0]
        if not odd_list:
            return "No matches"
        else:
            return find_index(min(odd_list), input_list)


def first(filter, input_list, input_count):
    if input_count > len(input_list):
        return "Invalid count"
    elif filter == "even":
        even_list = [x for x in input_list if x % 2 == 0]
        return even_list[:input_count]
    elif filter == "odd":
        odd_list = [x for x in input_list if x % 2 != 0]
        return odd_list[:input_count]


def last(filter, input_list, input_count):
    if input_count > len(input_list):
        return "Invalid count"
    elif filter == "even":
        even_list = [x for x in input_list if x % 2 == 0]
        if input_count > len(even_list):
            input_count = len(even_list)
        return even_list[len(even_list)-input_count:]
    elif filter == "odd":
        odd_list = [x for x in input_list if x % 2 != 0]
        if input_count > len(odd_list):
            input_count = len(odd_list)
        return odd_list[len(odd_list)-input_count:]


my_list = input().split(" ")
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
command = input()
while command != "end":
    command_list = command.split()
    if command_list[0] == "exchange":
        if not 0 <= int(command_list[1]) <= len(my_list) - 1:
            print("Invalid index")
        else:
            my_list = exchange(int(command_list[1]), my_list)
    elif command_list[0] == "max":
        print(max_even_odd(command_list[1], my_list))
    elif command_list[0] == "min":
        print(min_even_odd(command_list[1], my_list))
    elif command_list[0] == "first":
        print(first(command_list[2], my_list, int(command_list[1])))
    elif command_list[0] == "last":
        print(last(command_list[2], my_list, int(command_list[1])))
    command = input()
print(my_list)
