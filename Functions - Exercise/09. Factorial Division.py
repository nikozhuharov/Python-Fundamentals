def factorial(num: int):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total


def division(num_1, num_2):
    return factorial(num_1) / factorial(num_2)


n1 = int(input())
n2 = int(input())

print(f"{division(n1, n2):.2f}")

