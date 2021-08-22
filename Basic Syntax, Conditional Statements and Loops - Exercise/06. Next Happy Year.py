year = int(input())
l = []
year2 = year
flag = True

while True:
    year2 += 1
    n = year2
    while n > 0:
        digit = n % 10
        l.append(digit)
        n = int(n/10)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                flag = False
    if flag:
        print(year2)
        break
    l = []
    flag = True

