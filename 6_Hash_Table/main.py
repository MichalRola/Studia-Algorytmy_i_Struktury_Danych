class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for _ in range(size)]

    def search(self, key):
        for i in range(self.size):
            index = (self.hash_function(key) + self.c1*i + self.c2*i**2) % self.size
            if self.tab[index].key == key:
                return self.tab[index].data
            elif self.tab[index] is None:
                return None

    def insert(self, key, data):
        is_full = True
        for i in range(self.size):
            index = (self.hash_function(key) + self.c1*i + self.c2*i**2) % self.size
            if self.tab[index] is None or self.tab[index].key == key or self.tab[index].key is None:
                self.tab[index] = Element(key, data)
                is_full = False
                break
        if is_full is True:
            print('Table is full.')

    def remove(self, key):
        for i in range(self.size):
            index = (self.hash_function(key) + self.c1*i + self.c2*i**2) % self.size
            if self.tab[index].key == key:
                self.tab[index] = Element(None, None) #problem z usuwaniem rozwiązano poprzez przypisywanie None do klucza oraz wartości.

    def __str__(self):
        print_hash = '{'
        for i in self.tab:
            if i is None or i.key is None:
                print_hash += 'None, '
            else:
                print_hash += str(i.key) + ':' + str(i.data) + ', '
        print_hash = print_hash[:-2]
        print_hash += "}"
        return print_hash

    def hash_function(self, key):
        if isinstance(key, int):
            return key % self.size
        else:
            asci_key = 0
            for i in key:
                asci_key += ord(i)
            return asci_key % self.size


class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data


def test1(size, c1=1, c2=0):
    hash_tab = HashTable(size, c1, c2)
    hash_tab.insert(1, 'A')
    hash_tab.insert(2, 'B')
    hash_tab.insert(3, 'C')
    hash_tab.insert(4, 'D')
    hash_tab.insert(5, 'E')
    hash_tab.insert(18, 'F')
    hash_tab.insert(31, 'G')
    hash_tab.insert(8, 'H')
    hash_tab.insert(9, 'I')
    hash_tab.insert(10, 'J')
    hash_tab.insert(11, 'K')
    hash_tab.insert(12, 'L')
    hash_tab.insert(13, 'M')
    hash_tab.insert(14, 'N')
    hash_tab.insert(15, 'O')
    print(hash_tab)
    print(hash_tab.search(5))
    print(hash_tab.search(14))
    hash_tab.insert(5, 'Z')
    print(hash_tab.search(5))
    hash_tab.remove(5)
    print(hash_tab)
    print(hash_tab.search(31))
    hash_tab.insert("test", "W")
    print(hash_tab)


def test2(size, c1=1, c2=0):
    hash_tab = HashTable(size, c1, c2)
    hash_tab.insert(1*13, 'A')
    hash_tab.insert(2*13, 'B')
    hash_tab.insert(3*13, 'C')
    hash_tab.insert(4*13, 'D')
    hash_tab.insert(5*13, 'E')
    hash_tab.insert(6*13, 'F')
    hash_tab.insert(7*13, 'G')
    hash_tab.insert(8*13, 'H')
    hash_tab.insert(9*13, 'I')
    hash_tab.insert(10*13, 'J')
    hash_tab.insert(11*13, 'K')
    hash_tab.insert(12*13, 'L')
    hash_tab.insert(13*13, 'M')
    print(hash_tab)


test1(13)
test2(13)
test2(13, 0, 1)
test1(13, 0, 1)
