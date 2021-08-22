resources = {}
command = input()

while command != "stop":
    value = int(input())
    if command not in resources:
        resources[command] = value
    else:
        resources[command] += value
    command = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
