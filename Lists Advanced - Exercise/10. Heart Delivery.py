neighborhood = input().split("@")
neighborhood = [int(x) for x in neighborhood]
command = input()
last_index = 0
love_houses = 0
while command != "Love!":
    index = int(command.split()[1])
    last_index += index
    if last_index >= len(neighborhood):
        last_index = 0
    if neighborhood[last_index] == 0:
        print(f"Place {last_index} already had Valentine's day.")
    else:
        neighborhood[last_index] -= 2
        if neighborhood[last_index] == 0:
            print(f"Place {last_index} has Valentine's day.")
            love_houses += 1
    command = input()

print(f"Cupid's last position was {last_index}.")
if len(neighborhood) == love_houses:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - love_houses} places.")