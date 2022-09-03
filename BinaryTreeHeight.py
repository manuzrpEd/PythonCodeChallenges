'''
Compute the height of a binary tree.
https://app.codility.com/programmers/trainings/4/tree_height/
https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
https://favtutor.com/blogs/binary-tree-height
A binary tree is either an empty tree or a node (called the root) consisting of a single integer value and two further binary trees,
called the left subtree and the right subtree.

A path in a binary tree is a non-empty sequence of nodes that one can traverse by following the pointers.
The length of a path is the number of pointers it traverses.
More formally, a path of length K is a sequence of nodes P[0], P[1], ..., P[K], such that node P[I + 1] is the root of the left or right subtree of P[I], for 0 ≤ I < K.

The height of a binary tree is defined as the length of the longest possible path in the tree.
In particular, a tree consisting of only one node has height 0 and, conventionally, an empty tree has height −1.

Write a function:

    def solution(T)

that, given a non-empty binary tree T consisting of N nodes, returns its height.
For example, given tree T shown in the figure above, the function should return 2, as explained above.
Note that the values contained in the nodes are not relevant in this task.
'''

# For example, the sequence of nodes with values 5, 3, 21 is a path of length 2 in the tree from the above figure.

# The sequence of nodes with values 10, 1 is a path of length 1.

# The sequence of nodes with values 21, 3, 20 is not a valid path.

# For example, the tree shown in the above figure is of height 2.
# from extratypes import Tree
#
# def solution(T):
#     if not T:
#         return -1
#     length = 0
#     Tree = list(T).copy()
#     while True:
#         if Tree[1]:
#             length += 1
#             Tree = Tree[1]
#         else:
#             break
#     return length
#
#
#     return -1
#
# Tree = (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
#
# print("\n Solution: ", solution(Tree))

# define a Class Tree, to intiate the binary tree
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# def height(root):
#     # Check if the binary tree is empty
#     if root is None:
#         # If TRUE return 0
#         return 0
#         # Recursively call height of each node
#     leftAns = height(root.left)
#     rightAns = height(root.right)
#
#     # Return max(leftHeight, rightHeight) at each iteration
#     return max(leftAns, rightAns) + 1
#
#
# # Test the algorithm
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
#
# print("\n Root: ", root)
# print("Height of the binary tree is: " + str(height(root)))

# Import Collections libaray to use Queue Datastructure
import collections


# define a Class Tree, to intiate the binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root):
    # Set result variable to 0
    ans = 0
    # Initialise the queue
    queue = collections.deque()
    # Check if the tree has no nodes
    if root is None:
        return ans

    # Append the nodes to queue and process it in while loop until its empty
    queue.append(root)

    # Process in while loop until there are elements in queue

    while queue:
        currSize = len(queue)
        # Unless the queue is empty
        while currSize > 0:
            # Pop elements one-by-one
            currNode = queue.popleft()
            currSize -= 1

            # Check if the node has left/right child
            if currNode.left is not None:
                queue.append(currNode.left)
            if currNode.right is not None:
                queue.append(currNode.right)

        # Increment ans when currSize = 0
        ans += 1
    return ans


# Test the algorithm
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print("Height of the binary tree is: " + str(height(root)))


# def solution(T):
#     # write your code in Python 3.6
#     def height(T):
#         # write your code in Python 3.6
#         # Check if the binary tree is empty
#         if T is None:
#             # If TRUE return 0
#             return 0
#             # Recursively call height of each node
#         leftAns = height(T.l)
#         rightAns = height(T.r)
#
#         # Return max(leftHeight, rightHeight) at each iteration
#         return max(leftAns, rightAns) + 1
#
#     return height(T) - 1