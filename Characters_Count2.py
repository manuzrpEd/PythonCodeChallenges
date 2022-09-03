lst = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'o', 'a', 'b', 'b']
lst.append('end')

def cnt(lst, c=0):
  if len(lst) >= 2:
    item = lst.pop(0)
    c += 1
    if item == lst[0]:
      cnt(lst, c)
    else:
      print(f"item {item} found {c} times")
      cnt(lst)

cnt(lst)