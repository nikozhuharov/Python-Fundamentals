n = int(input())
register = {}

for i in range(n):
    command = input().split()
    if command[0] == "register":
        name = command[1]
        number = command[2]
        if name not in register:
            register[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")
    elif command[0] == "unregister":
        name = command[1]
        if name not in register:
            print(f"ERROR: user {name} not found")
        else:
            register.pop(name)
            print(f"{name} unregistered successfully")
for key, value in register.items():
    print(f"{key} => {value}")


