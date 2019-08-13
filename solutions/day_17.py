def eval(expression):
    stack = []

    for item in expression:
        if item == '-' or item == '+':
            stack.append(item)

        if item.isdigit():
            stack.append(item)

        if item == ')':
            num_1 = int(stack.pop())
            exp = stack.pop()
            num_2 = int(stack.pop())

            if exp == '-':
                stack.append(num_2 - num_1)
            else:
                stack.append(num_2 + num_1)

    if len(stack) == 2:
        return -1 * stack[1]
    return stack[0]

expression = '- (3 + ( 2 - 1 ) )'
expected = -4
result = eval(expression)
assert result == expected
print('eval({}) = {}'.format(expression, result))
print('Test pass.')