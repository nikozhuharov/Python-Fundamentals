def sum_even_odd(n):
    odd = 0
    even = 0
    str_n = str(n)
    for i in str_n:
        num_i = int(i)
        if num_i % 2 != 0:
            odd += num_i
        else:
            even += num_i
    print(f"Odd sum = {odd}, Even sum = {even}")


num = int(input())
sum_even_odd(num)
