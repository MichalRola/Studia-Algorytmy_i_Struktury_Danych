class LinkedList:
    def __init__(self):
        self.head = None

    def destroy(self):
        if self.head is not None:
            self.head = None
        else:
            print("Cannot destroy empty list.\n")
            return 1

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Cannot remove element from empty list.\n")
            return 1

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        current = self.head
        list_length = 0
        while current is not None:
            list_length += 1
            current = current.next
        return list_length

    def get(self):
        if self.head is not None:
            return self.head.data
        else:
            print("List is empty.\n")
            return None

    def __str__(self):
        if self.head is not None:
            print_list = ""
            current = self.head
            while current is not None:
                print_list = print_list + str(current.data) + "\n"
                current = current.next
            return print_list
        else:
            return "Empty list cannot be printed.\n"

    def add_end(self, data):
        current = self.head
        if current is None:
            self.add(data)
        else:
            while current is not None:
                if current.next is None:
                    new_node = Node(data)
                    current.next = new_node
                    break
                current = current.next

    def remove_end(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                if current.next.next is None:
                    current.next = None
                    break
                current = current.next
        else:
            print("Cannot remove element from empty list.\n")
            return 1

    def take(self, n):
        i = 1
        new_linked_list = LinkedList()
        current = self.head
        while i <= n and current is not None:
            new_linked_list.add_end(current.data)
            current = current.next
            i += 1
        return new_linked_list

    def drop(self, n):
        i = 1
        new_linked_list = LinkedList()
        current = self.head
        while current is not None:
            if i > n:
                new_linked_list.add_end(current.data)
            current = current.next
            i += 1
        return new_linked_list


class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None


def main():
    list_1 = LinkedList()
    print("List 1 length is equal: " + str(list_1.length()) + "\n")
    list_1.destroy()
    list_1.remove()
    list_1.remove_end()
    print("List 1 is empty: " + str(list_1.is_empty()) + "\n")
    list_1.add(('PW', 'Warszawa', 1915))
    list_1.add(('UJ', 'Kraków', 1364))
    list_1.add(('AGH', 'Kraków', 1919))
    list_1.add_end(('UW', 'Warszawa', 1915))
    list_1.add_end(('UP', 'Poznań', 1919))
    list_1.add_end(('PG', 'Gdańsk', 1945))
    print("List 1 after adding elements to it:\n" + str(list_1))
    list_1.remove()
    print("List 1 after removing 1-st element from it:\n" + str(list_1))
    list_1.remove_end()
    print("List 1 after removing last element from it:\n" + str(list_1))
    print("List 1 is empty: " + str(list_1.is_empty()) + "\n")
    print("List 1 length is equal: " + str(list_1.length()) + "\n")
    list_2 = list_1.take(2)
    print("List 2 created from 1-st 2 elements of List 1:\n" + str(list_2))
    list_3 = list_1.drop(2)
    print("List 3 created from last 2 elements of List 1:\n" + str(list_3))
    print("First element of the List 3: " + str(list_3.get())+"\n")
    list_1.destroy()
    print("List 1 after destroying it:\n" + str(list_1))
    print("List 1 1-st element after destroying it is: " + str(list_1.get())+"\n")


if __name__ == '__main__':
    main()
