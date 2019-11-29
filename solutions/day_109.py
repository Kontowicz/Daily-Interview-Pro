def is_operator(item):
    if item == '+' or item == '-' or item == '*' or item == '/':
        return True
    return False

def reverse_polish_notation(expr):
    stack = []

    for item in expr:
        if is_operator(item):
            a = stack.pop()
            b = stack.pop()
            if item == '+':
                stack.append(b + a)
            elif item == '-':
                stack.append(b - a)
            elif item == '*':
                stack.append(b * a)
            else:
                stack.append(b / a)
        else:
            stack.append(item)

    return stack.pop()

assert reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']) == -9
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
print('Test pass.')