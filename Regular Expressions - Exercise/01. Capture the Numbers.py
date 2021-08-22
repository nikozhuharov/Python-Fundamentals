import re
text = input()

while text:
    pattern = r"\d+"
    numbers = re.findall(pattern, text)
    for num in numbers:
        if num:
            print(num, end=" ")
    text = input()