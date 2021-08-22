def min_function (num_1, num_2, num_3):
    if num_1 <= num_2 and num_1 <= num_3:
        return num_1
    elif num_2 <= num_1 and num_2 <= num_3:
        return num_2
    else:
        return num_3


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(min_function(n1, n2, n3))