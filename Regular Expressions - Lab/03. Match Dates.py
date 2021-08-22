import re
pattern = r"(?P<Day>\d{2})(?P<Separator>[-./])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>[0-9]{4})"
text = input()
dates = re.finditer(pattern, text)
for date in dates:
    print(f'Day: {date.group("Day")}, Month: {date.group("Month")}, Year: {date.group("Year")}')
