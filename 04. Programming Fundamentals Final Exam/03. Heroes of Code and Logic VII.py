n = int(input())
heroes = {}
for _ in range(n):
    hero_input = input().split()
    heroes[hero_input[0]] = {"HP": int(hero_input[1]), "MP": int(hero_input[2])}

command = input()
while not command == "End":
    command_arg = command.split(" - ")
    if command_arg[0] == "CastSpell":
        hero = command_arg[1]
        MP = int(command_arg[2])
        spell = command_arg[3]
        if hero in heroes:
            if heroes[hero]["MP"] >= MP:
                heroes[hero]["MP"] -= MP
                print(f'{hero} has successfully cast {spell} and now has {heroes[hero]["MP"]} MP!')
            else:
                print(f"{hero} does not have enough MP to cast {spell}!")
    elif command_arg[0] == "TakeDamage":
        hero = command_arg[1]
        damage = int(command_arg[2])
        attacker = command_arg[3]
        if hero in heroes:
            heroes[hero]["HP"] -= damage
            if heroes[hero]["HP"] > 0:
                print(f'{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]["HP"]} HP left!')
            else:
                print(f"{hero} has been killed by {attacker}!")
                del heroes[hero]
    elif command_arg[0] == "Recharge":
        hero = command_arg[1]
        amount = int(command_arg[2])
        if heroes[hero]["MP"] + amount > 200:
            print(f"{hero} recharged for {200-heroes[hero]['MP']} MP!")
            heroes[hero]["MP"] = 200
        else:
            print(f"{hero} recharged for {amount} MP!")
            heroes[hero]["MP"] += amount
    elif command_arg[0] == "Heal":
        hero = command_arg[1]
        amount = int(command_arg[2])
        if heroes[hero]["HP"] + amount > 100:
            print(f"{hero} healed for {100-heroes[hero]['HP']} HP!")
            heroes[hero]["HP"] = 100
        else:
            print(f"{hero} healed for {amount} HP!")
            heroes[hero]["HP"] += amount
    command = input()

sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1]["HP"], x[0])))
for hero, value in sorted_heroes.items():
    print(hero)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")