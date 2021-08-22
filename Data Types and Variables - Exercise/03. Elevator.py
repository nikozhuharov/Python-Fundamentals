n = int(input())
p = int(input())
if n % p != 0:
    print(n//p+1)
else:
    print(n//p)