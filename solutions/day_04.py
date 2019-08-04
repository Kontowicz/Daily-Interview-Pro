class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                continue

            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()

        return len(stack) == 0


s = "()(){(())"
assert Solution().isValid(s) == False

s = ""
assert Solution().isValid(s) == True

s = "([{}])()"
assert Solution().isValid(s) == True

print('Test pass.')