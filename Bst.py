# Tree object of root connected to left and right subtree
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Bst:
    def __init__(self, arr):
        self.arr = arr
        self.root = None
        self.vals = []

    # Initialization method that creates tree's root for first value
    # Then self.insert method is called for insertion of every other element in inputted order
    def construct(self):
        arr = self.arr

        root = self.insert(None, arr.pop(0))
        self.root = root

        for i in arr:
            self.insert(root, i)

        print('Ascending order: ', end='\t')
        self.inOrder(root)
        print('\n"From top" order: ', end='\t')
        self.fromTop(root)
        print('\nLevel by level order: ')
        self.byLevels(root)

    # Recursive method that compares value to tree's node value and goes down the tree to either left or right subtree
    # If None is tree arg, creates one
    def insert(self, tree, val):
        if tree is None:
            return Tree(val)

        if val < tree.val:
            tree.left = self.insert(tree.left, val)
        elif val > tree.val:
            tree.right = self.insert(tree.right, val)

        return tree

    # Recursive method that prints elements of a tree in ascending order
    # Method goes from most left tree's node to most right node
    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.val, end=' ')
            self.inOrder(root.right)

    # Second recursive method for printing elements of a tree from top to left order
    # Method goes from root node and if possible goes down left, if not down right
    def fromTop(self, root):
        if root is not None:
            print(root.val, end=' ')
            self.fromTop(root.left)
            self.fromTop(root.right)

    # Third iterative and recursive method for printing elements of a tree one by one level
    # Method calls self.__printLevel() method until empty level is found
    def byLevels(self, root):
        self.__printLevel(root, 0)

        i = 1
        while self.vals:
            print(self.vals)
            self.vals = []
            self.__printLevel(root, i)
            i += 1

    # Start method that calls find min and max node's value recursive methods self.__recurFindMin()
    # and self.__recurFindMax()
    def findMinMax(self):
        root = self.root

        self.__recurFindMin(root)
        self.__recurFindMax(root)
        print('')

    # Recursive function for finding minimum node's value
    # Method always goes down the left side of the tree until leaf node is reached
    def __recurFindMin(self, root):
        if root.left is not None:
            self.__recurFindMin(root.left)
        else:
            print(f'\n\nMin value is: \t\t{root.val}')

    # Recursive function for finding maximum node's value
    # Method always goes down the right side of the tree until leaf node is reached
    def __recurFindMax(self, root):
        if root.right is not None:
            self.__recurFindMax(root.right)
        else:
            print(f'Max value is: \t\t{root.val}')

    # Start method that "popes" node of a tree
    # Firstly recursive self.__searchLevel() method is called to find node's level number
    # Secondly recursive self.__printLevel() method is called to print whole tree's level of a given number
    # Lastly recursive self.__removeNode() method is called to remove node, restructure and update tree
    def popNode(self, key):
        root = self.root

        level = self.__searchLevel(key, root)
        print(f'Level of {key} is: \t{level}')

        if level != -1:
            self.vals = []
            self.__printLevel(root, level)
            print(f'The whole level is: {self.vals}')

            root = self.__removeNode(key, root)

            print('New ascending order: ', end='\t')
            self.inOrder(root)
            print('\nNew "from top" order: ', end='\t')
            self.fromTop(root)
            print('\nNew level by level order: ')
            self.vals = []
            self.byLevels(root)

            self.root = root

    # Recursive method for finding node with value equal to a given key and returning its level number
    # Method goes down the tree either left or right side depending on key-value comparison
    def __searchLevel(self, key, root, level=0):
        if root is not None:

            if root.val == key:
                return level
            elif root.val > key:
                return self.__searchLevel(key, root.left, level + 1)
            else:
                return self.__searchLevel(key, root.right, level + 1)

        else:
            return -1

    # Recursive method for printing whole tree level (every node with the same height) of a given number
    def __printLevel(self, root, level, curr=0):
        if root is not None:

            if curr == level:
                self.vals.append(root.val)

            self.__printLevel(root.left, level, curr + 1)
            self.__printLevel(root.right, level, curr + 1)

    # Recursive method for finding, deleting and restructuring tree
    # Three cases are handled where node has 0, 1 or 2 children
    # In third case method always chooses right children
    def __removeNode(self, key, root):
        if root is not None:

            if root.val == key:

                # First and second case: at least one of the children is empty
                if root.left is None:
                    temp = root.right
                    return temp
                elif root.right is None:
                    temp = root.left
                    return temp

                # Third case: both children exist
                else:
                    new_root = root
                    new_child = root.right

                    while new_child.left is not None:
                        new_root = new_child
                        new_child = new_child.left

                    if new_root != root:
                        new_root.left = new_child.right
                    else:
                        new_root.right = new_child.right

                    root.val = new_child.val

                    return root

            elif root.val > key:
                root.left = self.__removeNode(key, root.left)
                return root
            else:
                root.right = self.__removeNode(key, root.right)
                return root

        else:
            return -1


if __name__ == '__main__':
    root = None

    arr = [8, 2, 5, 14, 1, 10, 12, 13, 6, 9]

    tree = Bst(arr)
    tree.construct()

    tree.findMinMax()

    tree.popNode(8)
