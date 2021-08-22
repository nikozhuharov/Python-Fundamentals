def is_perfect (num):
    total = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            total += i
    if num == total:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


n = int(input())
is_perfect(n)
