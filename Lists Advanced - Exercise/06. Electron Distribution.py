electrons = int(input())
n = 1
electrons_list =[]

while electrons > 0:
    layer = 2*pow(n, 2)
    if electrons > layer:
        electrons_list.append(layer)
    else:
        electrons_list.append(electrons)
    electrons -= layer
    n += 1

print(electrons_list)

