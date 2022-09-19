def reverse(root):
    reverted_root = []
    for i in range(len(root)-1,-1,-1):
        reverted_root.append(root[i])
    return reverted_root

