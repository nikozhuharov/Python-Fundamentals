def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def add_and_subtract(num_1, num_2, num_3):
    return subtract(sum_numbers(num_1, num_2), num_3)


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(add_and_subtract(n1, n2, n3))



