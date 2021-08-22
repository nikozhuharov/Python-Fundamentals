health = 100
bitcoins = 0
rooms = input().split('|')
dead = False
for i in range(len(rooms)):
    room = rooms[i].split(" ")
    command = room[0]
    num = int(room[1])
    if command == "potion":
        if 100 - health >= num:
            print(f"You healed for {num} hp.")
            health += num
        else:
            print(f"You healed for {100 - health} hp.")
            health = 100
        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {num} bitcoins.")
        bitcoins += num
    else:
        health -= num
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i+1}")
            dead = True
            break
if not dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

