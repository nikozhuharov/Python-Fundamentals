def palindrome(list1):
    for num in list1:
        n = len(num)
        half = n // 2
        is_palindrome = True
        for i in range(half):
            if num[i] != num[-(i+1)]:
                is_palindrome = False
        if is_palindrome:
            print("True")
        else:
            print("False")


my_list = input().split(", ")
palindrome(my_list)



