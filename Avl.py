import time
import math


# Tree object of root connected to left and right subtree
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Avl:
    def __init__(self, arr):
        arr.sort()
        self.arr = arr
        self.meds = []
        self.root = None
        self.vals = []
        self.sub_height = 0

    # Initialization method that creates tree's root for first value
    # self.medians is called to create input array similar to Bts' one but made of medians of every half list
    # Then self.insert method is called for insertion of every other element in medians' list
    def construct(self):
        self.medians()
        meds = self.meds

        root = self.insert(None, meds.pop(0))
        self.root = root

        for i in meds:
            self.insert(root, i)

        print('In-order: ', end='\t')
        self.inOrder(root)
        print('\nPre-order: ', end='\t')
        self.preOrder(root)
        print('\nDesc-order: ', end='')
        self.descOrder(root)
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

    # Iterative method that divide inputted sorted lists in half and find its medians
    # Dividing is done by levels, so first all 1. halves, then all 2. halves etc.
    def medians(self):
        arr = self.arr
        n = len(arr)
        meds = []
        queue = []

        mid = n // 2 - 1 if n % 2 == 0 else n // 2
        median = arr[mid]

        meds.append(median)

        left = arr[:mid]
        right = arr[mid + 1:]

        queue.append(left)
        queue.append(right)

        while queue:
            curr = queue.pop(0)
            n = len(curr)

            if n == 0:
                continue

            if n == 1:
                meds.append(curr[0])
                continue

            mid = n // 2 - 1 if n % 2 == 0 else n // 2
            median = curr[mid]

            meds.append(median)

            left = curr[:mid]
            right = curr[mid + 1:]
            queue.append(left)
            queue.append(right)

        self.meds = meds

    # Start method for printing tree's values in different orders
    # Values are printed in-order, pre-order, descending order and by levels
    def printInfo(self):
        root = self.root

        print('\nIn-order: ', end='\t')
        self.inOrder(root)
        print('\nPre-order: ', end='\t')
        self.preOrder(root)
        print('\nDesc-order: ', end='')
        self.descOrder(root)
        print('\nLevel by level order: ')
        self.vals = []
        self.byLevels(root)
        print('')

    # Recursive method that prints elements of a tree in ascending order
    # Method goes from most left tree's node to most right node
    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.val, end=' ')
            self.inOrder(root.right)

    # Second recursive method for printing elements of a tree from top to left order
    # Method goes from root node and if possible goes down left, if not down right
    def preOrder(self, root):
        if root is not None:
            print(root.val, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

    # Third recursive method for printing elements in descending order
    # Method goes from root node and if possible goes down right, if not down left
    def descOrder(self, root):
        if root is not None:
            self.descOrder(root.right)
            print(root.val, end=' ')
            self.descOrder(root.left)

    # Fourth iterative and recursive method for printing elements of a tree one by one level
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

        print('Path to min is: ', end=' ')
        self.__recurFindMin(root)
        print('\nPath to max is: ', end=' ')
        self.__recurFindMax(root)
        print('')

    # Recursive function for finding minimum node's value
    # Method always goes down the left side of the tree until leaf node is reached
    def __recurFindMin(self, root):
        if root.left is not None:
            print(root.val, end=' ')
            self.__recurFindMin(root.left)
        else:
            print(f'\nMin value is: \t{root.val}')

    # Recursive function for finding maximum node's value
    # Method always goes down the right side of the tree until leaf node is reached
    def __recurFindMax(self, root):
        if root.right is not None:
            print(root.val, end=' ')
            self.__recurFindMax(root.right)
        else:
            print(f'\nMax value is: \t{root.val}')

    # Start method that "popes" node of a tree
    # Firstly recursive self.__searchLevel() method is called to find node's level number
    # Secondly recursive self.__printLevel() method is called to print whole tree's level of a given number
    # Lastly recursive self.__removeNode() method is called to remove node, restructure and update tree
    def popNode(self, key):
        root = self.root

        level, subtree_root = self.__searchLevel(key, root)
        print(f'Level of {key} is: \t{level}')

        if level != -1:
            self.vals = []
            self.__printLevel(root, level)
            print(f'The whole level is: {self.vals}')

            root = self.__removeNode(key, root)

            self.root = root

    # Recursive method for finding node with value equal to a given key and returning its level number
    # Method goes down the tree either left or right side depending on key-value comparison
    def __searchLevel(self, key, root, level=0):
        if root is not None:

            if root.val == key:
                return level, root
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

    # Start method for finding subtree by its root value
    # and deleting it by calling recursive self.__findSubtree() method
    def popSubtree(self, key):
        root = self.root
        self.root = self.__findSubtree(key, root)
        print(f'\nThe height of the subtree is: {self.sub_height}')

    # Simple recursive method similar to self.__searchLevel()
    # Method goes down the tree until subtree's root node of given value is found
    # Then self.__postOrderRemove(root) is called to remove subtree
    # This method returns every changed node so main tree is updated
    def __findSubtree(self, key, root):
        if root.val > key:
            root.left = self.__findSubtree(key, root.left)

            return root
        elif root.val < key:
            root.right = self.__findSubtree(key, root.right)

            return root
        else:
            print('\nSubtree in pre-order: ', end='\t')
            self.preOrder(root)

            root = self.__postOrderRemove(root)

            return root

    # Recursive function for removing subtree of given root node
    # Nodes are removed one by one in post-order
    # Height of subtree is updated every in every recursive step
    def __postOrderRemove(self, root, level=0):
        if root is not None:
            root.left = self.__postOrderRemove(root.left, level + 1)
            root.right = self.__postOrderRemove(root.right, level + 1)

            self.sub_height = max(self.sub_height, level)

            return None

    # Start method that for balancing tree using DSW algorithm
    # Firstly self.__dsw_first() method is called to create vine tree from given tree connected to dummy node
    def dsw(self):
        root = self.root

        dummy = Tree(0)
        dummy.right = root

        vine_height = self.__dswFirst(dummy)

        root = self.__dswSecond(dummy, vine_height)
        self.root = root

    # Iterative method for creating vine tree from given tree connected to dummy node, first phase of DSW algorithm
    # Loop goes down right the tree, if left node is found it - rotates right
    # Rotation replace root's left node (oldTemp) with root's-left node's right node (temp)
    # Then oldTemp is made right node of temp, which is next set as new root node
    def __dswFirst(self, root):
        temp = root.right
        n = 0

        while temp:

            if temp.left:
                oldTemp = temp
                temp = temp.left
                oldTemp.left = temp.right
                temp.right = oldTemp
                root.right = temp
            else:
                n += 1
                root = temp
                temp = temp.right

        return n

    # Iterative method for balancing tree from given vine tree connected to dummy node, second phase of DSW algorithm
    # Firstly self.__leftRotate() is called once to rotate left every second node
    # Then self.__leftRotate() is called inside loop for rotating transformed vine
    def __dswSecond(self, root, vine_height):
        balanced_height = int(math.log2(vine_height + 1))
        operations_num = 2 ** balanced_height - 1

        self.__leftRotate(root, vine_height - operations_num)

        for m in [operations_num // 2 ** i for i in range(1, balanced_height + 1)]:
            self.__leftRotate(root, m)

        return root.right

    # Iterative method for rotating left nodes in the given tree
    # Loop goes down right the tree - dummy node (root), root's right node (oldTemp) and oldTemp's right node (temp)
    # Temp is made right node of root node and oldTemp is made left node of temp
    # Then temp is made new root
    def __leftRotate(self, root, m):
        temp = root.right

        for i in range(m):
            oldTemp = temp
            temp = temp.right
            root.right = temp
            oldTemp.right = temp.left
            temp.left = oldTemp
            root = temp
            temp = temp.right

if __name__ == '__main__':
    root = None

    arr = [1, 2, 7, 12, 13, 6, 8, 4, 10, 3, 5, 9, 11]

    tree = Avl(arr)
    tree.construct()
    tree.printInfo()

    start = time.perf_counter_ns()

    # Choose function:

    # tree.findMinMax()

    # tree.popNode(8)

    # tree.popSubtree(12)

    # tree.dsw()

    end = time.perf_counter_ns()
    print('---------------------------')
    print(f'Computed in {end - start}ns')
    print('---------------------------')

    tree.printInfo()
