'''
https://app.codility.com/programmers/trainings/7/arr_list_len/
'''

# For example, for array A such that:
A = [None]*5
A[0] =  1
A[1] =  4
A[2] = -1
A[3] =  3
A[4] =  2

def solution(A):
    if A[0]==-1:
        return 1
    n = 1
    K = A[0]
    while True:
        K = A[K]
        n += 1
        if K==-1:
            return n
    return -1

print("\n Solution: ", solution(A))