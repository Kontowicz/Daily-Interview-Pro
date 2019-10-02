class minStack(object):
    def __init__(self):
        self.stak = []
        self.min = 0

    def push(self, x):
        if self.stak == []:
            self.min = x
            self.stak.append(x)
        else:
            if x >= self.min:
                self.stak.append(x)
            else:
                self.stak.append(2*x-self.min)
                self.min = x

    def pop(self):
        y = self.stak.pop()
        if y >= self.min:
            return y
        else:
            self.min = 2*self.min - y
            return y

    def top(self):
        return self.stak[-1]

    def getMin(self):
        return self.min

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2