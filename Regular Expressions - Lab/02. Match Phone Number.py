import re
pattern = r"\+359(\s|-)2(\1)\d{3}(\1)\d{4}\b"
my_list = []
text = input()
numbers = re.finditer(pattern, text)
for num in numbers:
    my_list.append(num.group())
print(", ".join(my_list))