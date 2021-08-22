import re
n = int(input())
pattern = r"(^\$|^\%)([A-Z][a-z]{2,})(\1):\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

for _ in range(n):
    is_match = False
    text = input()
    matches = re.finditer(pattern, text)
    for match in matches:
        print(f"{match.group(2)}: {chr(int(match.group(4)))}{chr(int(match.group(5)))}{chr(int(match.group(6)))}")
        is_match = True
    if not is_match:
        print("Valid message not found!")

