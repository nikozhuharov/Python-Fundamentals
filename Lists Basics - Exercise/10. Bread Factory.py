energy = 100
coins = 100
events = input().split("|")
is_closed = False
for event in events:
    event_list = event.split("-")
    name = event_list[0]
    num = int(event_list[1])
    if name == "rest":
        if energy + num >= 100:
            print(f"You gained {100-energy} energy.")
            energy = 100
        else:
            print(f"You gained {num} energy.")
            energy += num
        print(f"Current energy: {energy}.")
    elif name == "order":
        if energy >= 30:
            energy -= 30
            coins += num
            print(f"You earned {num} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        coins -= num
        if coins > 0:
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
