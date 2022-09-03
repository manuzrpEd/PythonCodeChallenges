# https://www.geeksforgeeks.org/maximum-number-of-leaf-nodes-that-can-be-visited-within-the-given-budget/

# Python3 program to calculate the maximum number of leaf
# nodes that can be visited within the given budget
 
# struct that represents a node of the tree
class Node:
    # Constructor to set the data of
    # the newly created tree node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
# Priority queue to store the levels
# of all the leaf nodes
pq = []
 
# Level order traversal of the binary tree
def levelOrder(root):
 
    q = []
    level = 0
 
    # If tree is empty
    if (root == None):
        return
 
    q.append(root)
 
    while (True) :
 
        Len = len(q)
        if (Len == 0):
            break
        level+=1
        while (Len > 0) :
 
            temp = q[0]
            del q[0]
 
            # If left child exists
            if (temp.left != None):
                q.append(temp.left)
 
            # If right child exists
            if (temp.right != None):
                q.append(temp.right)
 
            # If node is a leaf node
            if (temp.left == None and temp.right == None):
             
                pq.append(level)
                pq.sort()
                pq.reverse()
             
            Len-=1
     
    return pq
 
# Function to calculate the maximum number of leaf nodes
# that can be visited within the given budget
def countLeafNodes(root, budget):
 
    pq = levelOrder(root)
 
    # Variable to store the count of
    # number of leaf nodes possible to visit
    # within the given budget
    count = 0
 
    while (len(pq) != 0) :
 
        # Removing element from
        # min priority queue one by one
        val = pq[0]
        del pq[0]
 
        # If current val is under budget, the
        # node can be visited
        # Update the budget afterwards
        if (val <= budget) :
            count+=1
            budget -= val
         
        else:
            break
         
    return count
 
root = Node(10)
root.left = Node(8)
root.right = Node(15);
root.left.left = Node(3)
root.left.left.right = Node(13)
root.right.left = Node(11)
root.right.right = Node(18)
 
budget = 8
 
print(countLeafNodes(root, budget))
 
# This code is contributed by suresh07.