class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_val = None

    def push(self, val):
        if self.stack == []:
            self.max_val = val
            self.stack.append(val)
            return
        if self.max_val >= val:
            self.stack.append(val)
            return
        self.stack.append(((2*val) - self.max_val))
        self.max_val = val

    def pop(self):
        value = self.stack.pop()
        if value < self.max_val:
            return value
        self.max_val = ((2*self.max_val) - value)
        return value

    def max(self):
        return self.max_val

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
v = s.max()
print(v)
assert v == 3

s.pop()
s.pop()
v = s.max()
print(v)
assert v == 2
