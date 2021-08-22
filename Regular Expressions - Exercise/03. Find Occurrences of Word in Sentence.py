import re
counter =0
text = input()
word = input()
pattern = rf"\b{word}\b"

words = re.finditer(pattern, text, re.IGNORECASE)
for i in words:
    counter += 1

print(counter)
