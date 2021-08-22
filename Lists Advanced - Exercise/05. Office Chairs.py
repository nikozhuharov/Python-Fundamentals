n = int(input())
surplus = 0
shortage = False
for i in range(1, n+1):
    room = input().split()
    chairs = room[0]
    people = int(room[1])
    if len(chairs) < people:
        print(f"{people - len(chairs)} more chairs needed in room {i}")
        shortage = True
    else:
        surplus += len(chairs) - people
if not shortage:
    print(f"Game On, {surplus} free chairs left")



