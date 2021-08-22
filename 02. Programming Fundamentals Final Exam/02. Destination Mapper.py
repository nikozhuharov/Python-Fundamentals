import re
text = input()
points = 0
destinations = []
pattern = r"(\=|\/)(?P<Destination>[A-Z][A-Za-z]{2,})(\1)"
matches = re.finditer(pattern, text)
for match in matches:
    destinations.append(match.group("Destination"))
    points += len(match.group("Destination"))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")