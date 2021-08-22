version = input().split(".")
number_list = [int(x) for x in version]
number = number_list[0]*100 + number_list[1]*10 + number_list[2]
next_number = number + 1
next_number_str = str(next_number)
print(f"{next_number_str[0]}.{next_number_str[1]}.{next_number_str[2]}")