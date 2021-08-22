def is_force_user_available(reg, f_u):
    av = False
    for v in reg.values():
        if f_u in v:
            av = True
            break
    if not av:
        return False
    return True


command = input()
register = {}

while command != "Lumpawaroo":
    if '|' in command:
        force_side, force_user = command.split(" | ")
        if force_side not in register:
            if not is_force_user_available(register, force_user):
                register[force_side] = [force_user]
        else:
            if not is_force_user_available(register, force_user):
                register[force_side].append(force_user)

    if '->' in command:
        force_user, force_side = command.split(" -> ")
        if is_force_user_available(register, force_user):
            for value in register.values():
                if force_user in value:
                    value.remove(force_user)
        if force_side in register:
            register[force_side].append(force_user)
        else:
            register[force_side] = [force_user]
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for key, value in register.items():
    my_list = list(value)
    my_list.sort()
    register[key] = my_list

register = dict(sorted(register.items(), key=lambda x: x[0]))
register = dict(sorted(register.items(), key=lambda x: len(x[1]), reverse=True))

for key, value in register.items():
    if len(value) != 0:
        print(f"Side: {key}, Members: {len(value)}")
        for i in range(0, len(value)):
            print(f"! {value[i]}")

