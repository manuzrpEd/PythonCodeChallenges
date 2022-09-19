# implement this function
def reverse(root):
    reverted_root = []
    for i in range(len(root)-1,-1,-1):
        reverted_root.append(root[i])
    return reverted_root

lst = [64, 7, 28, 43, 3]
print("\nSolution: ", reverse(lst))

lst = [12]
print("\nSolution: ", reverse(lst))

lst = [1, 3, 12, 12, 12, 13, 1, 14, 5]
print("\nSolution: ", reverse(lst))

