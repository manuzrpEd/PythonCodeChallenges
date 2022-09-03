# efficient search algorithm using the fact that a list is sorted
# Binary Search

def BinarySearch(val, lys):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    if index!=-1:
        return True
    else:
        return False

L=[1,4,8,10]
n=10
print(BinarySearch(n,L))