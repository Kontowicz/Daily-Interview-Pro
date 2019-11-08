import math

def is_palindrome(n):
    num = []

    while n != 0:
        num.append(n%10)
        n = n // 10

    return num == num[::-1]

assert is_palindrome(1234321) == True
print(is_palindrome(1234321))

assert is_palindrome(1234322) == False
print(is_palindrome(1234322))

print('Test pass.')