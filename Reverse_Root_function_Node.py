def reverse(root):
    prev = None
    current = root.head
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    root.head = prev

