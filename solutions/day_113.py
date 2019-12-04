def find_palindrome(s):
    occurence = {}
    for item in s:
        if item in occurence:
            occurence[item] = occurence[item] + 1
        else:
            occurence[item] = 1
    odd = 0
    for key, value in occurence.items():
        if value % 2 == 1:
            odd += 1

    if odd > 1:
        return None

    to_return = ''
    last = []
    for key, value in occurence.items():
        if value % 2 == 1:
            last = [key, float(value)]
        else:
            to_return = to_return[0:len(to_return)//2] + (key * value) + to_return[len(to_return)//2::]

    return (last[0] * int(last[1]//2)) + to_return[0:len(to_return)//2] + last[0] + to_return[len(to_return)//2::] + (last[0] * int(last[1]//2))

assert find_palindrome('momom') == 'momom'
print(find_palindrome('momom'))
print('Test pass.')