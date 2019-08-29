class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, val):
        while len(self.stack_1) != 0:
            self.stack_2.append(self.stack_1.pop())

        self.stack_1.append(val)

        while len(self.stack_2) != 0:
            self.stack_1.append(self.stack_2.pop())

    def dequeue(self):
        if len(self.stack_1) == 0:
            return None

        return self.stack_1.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3