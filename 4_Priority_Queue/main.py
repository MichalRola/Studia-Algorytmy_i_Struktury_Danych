class PriorityQueue:
    def __init__(self):
        self.tab = []

    def is_empty(self):
        return not bool(self.tab)

    def peek(self):
        return self.tab[0].value

    def dequeue(self):
        if self.is_empty():
            return None
        popped = self.tab[0].value
        j = 0
        self.tab[j] = self.tab[-1]
        self.tab.pop(-1)
        while (self.right(j) + 1) <= len(self.tab) and self.tab[j] < max(self.tab[self.left(j)], self.tab[self.right(j)]):
            if self.tab[self.left(j)] > self.tab[self.right(j)]:
                self.tab[j], self.tab[self.left(j)] = self.tab[self.left(j)], self.tab[j]
                j = self.left(j)
            else:
                self.tab[j], self.tab[self.right(j)] = self.tab[self.right(j)], self.tab[j]
                j = self.right(j)
        if self.left(j)+1 == len(self.tab):
            if self.tab[self.left(j)] > self.tab[j]:
                self.tab[j], self.tab[self.left(j)] = self.tab[self.left(j)], self.tab[j]
        return popped

    def enqueue(self, value, priority):
        self.tab.append(Element(value, priority))
        j = len(self.tab) - 1
        while j > 0 and self.tab[self.parent(j)] < self.tab[j]:
            self.tab[j], self.tab[self.parent(j)] = self.tab[self.parent(j)], self.tab[j]
            j = self.parent(j)

    def left(self, elem):
        return (2 * elem) + 1

    def right(self, elem):
        return (2 * elem) + 2

    def parent(self, elem):
        return (elem - 1)//2

    def print_tab(self):
        print('{', end=' ')
        if self.is_empty() is False:
            for k in range(len(self.tab) - 1):
                print(self.tab[k], end=', ')
            if self.tab[len(self.tab) - 1]:
                print(self.tab[len(self.tab) - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < len(self.tab):
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


class Element:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        if isinstance(other, int):
            return self.priority < other
        return self.priority < other.priority

    def __gt__(self, other):
        if isinstance(other, int):
            return self.priority > other
        return self.priority > other.priority

    def __str__(self):
        return str(self.priority) + ':' + str(self.value)


# utworzenie pustej kolejki
q = PriorityQueue()
# użycie w pętli enqueue do wpisana do niej elementów,
# których klucze będą brane z listy [4, 7, 6, 7, 5, 2, 2, 1],
# a odpowiadające im wartości będą kolejnymi literami z napisu "ALGORYTM"
for i in range(8):
    number = [4, 7, 6, 7, 5, 2, 2, 1]
    text = ["A", "L", "G", "O", "R", "Y", "T", "M"]
    q.enqueue(text[i], number[i])
# wypisanie aktualnego stanu kolejki w postaci kopca
q.print_tree(0, 0)
# wypisanie aktualnego stanu kolejki w postaci tablicy
q.print_tab()
# użycie dequeue do odczytu (i wypisania)  pierwszej  danej z kolejki
print(q.dequeue())
# użycie  peek do odczytu (i wypisania) kolejnej  danej
print(q.peek())
# wypisanie aktualnego stanu kolejki w postaci tablicy
q.print_tab()
# opróżnienie kolejki z wypisaniem usuwanych danych
while q.is_empty() is False:
    print(q.dequeue())
# wypisanie opróżnionej kolejki w postaci tablicy
q.print_tab()
