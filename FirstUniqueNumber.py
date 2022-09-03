'''
Find the first unique number in a given sequence.
A non-empty array A consisting of N integers is given. The unique number is the number that occurs exactly once in array A.
'''

def solution(A):
    assert type(A) is list, "A is not a list"
    if len(A)==1:
        return A[0]
    else:
        # copy list
        B = A.copy()
        # sort list
        A.sort()
        unique = []
        # append unique numbers
        for i in range(len(A)):
            if (i==0) and (A[0] != A[1]):
                unique.append(A[0])
            elif (i == len(A)-1) and (A[-1] != A[-2]):
                unique.append(A[-1])
            elif (A[i-1] != A[i]) and (A[i+1] != A[i]):
                unique.append(A[i])
        # get unique numbers from original list
        B = [b for b in B if b in unique]
        # return -1 if there is no unique number in the list
        if B != []:
            return B[0]
        else:
            return -1

# For example, the following array A contains two unique numbers (5 and 2).:
A = [None]*6
A[0] = 4
A[1] = 10
A[2] = 5
A[3] = 4
A[4] = 2
A[5] = 10

print("\n Array: ", A)
print("\n Solution: ", solution(A))

# For example, given:
A = [None]*6
A[0] = 1
A[1] = 4
A[2] = 3
A[3] = 3
A[4] = 1
A[5] = 2
print("\n Array: ", A)
print("\n Solution: ", solution(A))

# Given array A such that:
A = [None]*4
A[0] = 6
A[1] = 4
A[2] = 4
A[3] = 6
print("\n Array: ", A)
print("\n Solution: ", solution(A))

