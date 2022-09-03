# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Given a string of 3 characters, extract pairwise characters, 
# order pairs alphabetically, then return the first one

def solution(S):
    # write your code in Python 3.6
    lst=[]
    for i in range(1,len(S)+1):
        lst.append(S[:i-1] + S[i:])
    print("list: ",lst)
    lst=list(set(lst))
    lst.sort()
    return lst[0]
    pass

S="fox"
print(solution(S))