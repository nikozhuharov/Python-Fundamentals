max = 0
divisor = int(input())
bound = int(input())
for i in range (1, bound+1):
    if i % divisor == 0:
        max = i
print(max)
