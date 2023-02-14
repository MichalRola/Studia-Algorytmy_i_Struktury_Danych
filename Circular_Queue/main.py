class QueuedTable:
    def __init__(self, size=5):
        self.table = [None for _ in range(size)]
        self.save_index = 0
        self.read_index = 0

    def relocation(self, size):
        old_size = len(self.table)
        return [self.table[j] if j < old_size else None for j in range(size)]

    def is_empty(self):
        if self.save_index == self.read_index:
            return True
        else:
            return False

    def peek(self):
        return self.table[self.read_index]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            while self.table[self.read_index] is None:
                if self.read_index == len(self.table) - 1:
                    self.read_index = 0
                else:
                    self.read_index += 1
            value = self.table[self.read_index]
            self.table[self.read_index] = None
            if self.read_index == len(self.table) - 1:
                self.read_index = 0
            else:
                self.read_index += 1
            return value

    def enqueue(self, data):
        self.table[self.save_index] = data
        if self.save_index == len(self.table) - 1:
            self.save_index = 0
        else:
            self.save_index += 1
        if self.save_index == self.read_index:
            new_size = len(self.table) * 2
            self.table = self.relocation(new_size)
            for x in range(self.save_index, new_size // 2 - self.save_index + 1):
                self.table[x], self.table[x + new_size // 2] = self.table[x + new_size // 2], self.table[x]
            self.read_index = self.read_index + new_size // 2

    def print_std(self):
        print(self.table)

    def print_queue(self):
        p = self.read_index
        print("[", end='')
        while p != self.save_index - 1:
            print(self.table[p], end=', ')
            if p == len(self.table) - 1:
                p = 0
            else:
                p += 1
        print(str(self.table[p]) + "]")


queue = QueuedTable()
for i in range(1, 5):
    queue.enqueue(i)
print(queue.dequeue())
print(queue.peek())
queue.print_queue()
for i in range(5, 9):
    queue.enqueue(i)
queue.print_std()
while not queue.is_empty():
    print(queue.dequeue())
queue.print_queue()
