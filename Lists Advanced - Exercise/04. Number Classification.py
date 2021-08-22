def is_positive(num: int):
    if num >= 0:
        return True
    else:
        return False


def is_even(num: int):
    if num % 2 == 0:
        return True
    else:
        return False


positive_list = []
negative_list = []
even_list = []
odd_list = []

numbers = input().split(", ")
numbers_int = list(map(int, numbers))

for num in numbers_int:
    if is_positive(num):
        positive_list.append(str(num))
    else:
        negative_list.append(str(num))
    if is_even(num):
        even_list.append(str(num))
    else:
        odd_list.append(str(num))

print("Positive: " + ', '.join(positive_list))
print("Negative: " + ', '.join(negative_list))
print("Even: " + ', '.join(even_list))
print("Odd: " + ', '.join(odd_list))