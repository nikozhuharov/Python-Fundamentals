factor = int(input())
count = int(input())
num_list = []
f = factor

for i in range (count):
    num_list.append(f)
    f += factor

print(num_list)