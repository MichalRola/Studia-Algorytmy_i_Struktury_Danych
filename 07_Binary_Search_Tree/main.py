class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self, key, node=None):
        if self.root is None:
            return self.root
        if node is None:
            node = self.root
        if key == node.key:
            return node.value
        elif key > node.key:
            return self.search(key, node.right)
        elif key < node.key:
            return self.search(key, node.left)

    def insert(self, key, value, node=None):
        if self.root is None:
            self.root = TreeNode(key, value)
        if node is None:
            node = self.root
        if key < node.key:
            if node.left is None:
                new_node = TreeNode(key, value)
                node.left = new_node
            else:
                node.left = self.insert(key, value, node.left)
        elif key > node.key:
            if node.right is None:
                new_node = TreeNode(key, value)
                node.right = new_node
            else:
                node.right = self.insert(key, value, node.right)
        else:
            node = TreeNode(key, value, node.left, node.right)
        return node

    def delete(self, key, node=None):
        if self.root is None:
            return self.root
        if node is None:
            node = self.root
        if key < node.key:
            node.left = self.delete(key, node.left)
        elif key > node.key:
            node.right = self.delete(key, node.right)
        else:
            if node.left is None:
                temp = node.right
                TreeNode.node = None
                return temp
            elif node.right is None:
                temp = node.left
                TreeNode.node = None
                return temp
            temp = self.smallest_key(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self.delete(temp.key, node.right)
        return node

    def smallest_key(self, node):
        while node.left is not None:
            node = node.left
        return node

    def __str__(self):
        return self.print(self.root)

    def print(self, node):
        if node is None:
            return ''
        if node is not None:
            return self.print(node.left) + " " + str(node.key) + ":" + str(node.value) + " " + self.print(node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, node=None):
        if node is None:
            return 0
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.left, lvl + 5)


class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


# utworzenie pustego drzewa BST
binTree = BinaryTree()
# dodawanie element??w
binTree.insert(50, 'A')
binTree.insert(15, 'B')
binTree.insert(62, 'C')
binTree.insert(5, 'D')
binTree.insert(20, 'E')
binTree.insert(58, 'F')
binTree.insert(91, 'G')
binTree.insert(3, 'H')
binTree.insert(8, 'I')
binTree.insert(37, 'J')
binTree.insert(60, 'K')
binTree.insert(24, 'L')
# wy??wietl drzewo 2D
binTree.print_tree()
# wy??wietl zawarto???? drzewa jako list?? od najmniejszego do najwi??kszego klucza w formie klucz:warto????
print(binTree)
# znajd?? klucz 24 i wypisz warto????
print(binTree.search(24))
# zaktualizuj warto???? "AA" dla klucza 20
binTree.insert(20, 'AA')
# dodaj element 6:M
binTree.insert(6, 'M')
# usu?? element o kluczu 62
binTree.delete(62)
# dodaj element 59:N
binTree.insert(59, 'N')
# dodaj element 100:P
binTree.insert(100, 'P')
# usu?? element o kluczu 8
binTree.delete(8)
# usu?? element o kluczu 15
binTree.delete(15)
# dodaj element 55:R
binTree.insert(55, 'R')
# usu?? element o kluczu 50
binTree.delete(50)
# usu?? element o kluczu 5
binTree.delete(5)
# usu?? element o kluczu 24
binTree.delete(24)
# wypisz wysoko???? drzewa
print(binTree.height())
# wy??wietl zawarto???? drzewa jako list?? od najmniejszego do najwi??kszego klucza w formie klucz:warto????
print(binTree)
# wy??wietl drzewo 2D
binTree.print_tree()
