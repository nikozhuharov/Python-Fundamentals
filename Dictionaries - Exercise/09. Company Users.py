command = input()
records = {}

while command != "End":
    company, id = command.split(" -> ")
    if company not in records:
        records[company] = []
    if id not in records[company]:
        records[company].append(id)
    command = input()

records = dict(sorted(records.items(), key=lambda x: x[0]))

for key, value in records.items():
    print(key)
    for i in value:
        print(f"-- {i}")