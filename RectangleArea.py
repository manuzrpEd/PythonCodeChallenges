'''
https://app.codility.com/programmers/trainings/2/rectangle_builder_greater_area/

Write a function:

    def solution(A, X)

that, given an array A of N integers
(containing the lengths of the available pieces of fence) and an integer X,
returns the number of different ways of building a rectangular pen satisfying the above conditions.
The function should return −1 if the result exceeds 1,000,000,000.
'''

def solution(A, X):
    '''
    A: array
    X: minimum area length. The area of the pen must be greater than or equal to a given threshold X.
    '''
    if (X<1) or (X>1000000000):
        return -1
    # keep pairwise pens
    count_A = [A.count(e) for e in A]
    candidates = [A[i] for i in range(len(A)) if count_A[i]>=2]
    count_candidates = [candidates.count(e) for e in candidates]
    # create candidates set, allowing for squares:
    candidates_set = []
    for i in range(len(candidates)):
        if candidates[i] not in candidates_set:
            cnt_candidates = int(count_candidates[i]/2)
            for j in range(cnt_candidates):
                candidates_set.append(candidates[i])
    products = []
    for x in range(len(candidates_set)):
        for y in range(x,len(candidates_set)):
            if y>x:
                products.append((candidates_set[x], candidates_set[y]))
    products_set = list(set(products))
    products = [products_set[i][0]*products_set[i][1] for i in range(len(products_set))]
    areas = [e for e in products if e>=X]
    length = len(areas)
    if length<1000000000:
        return length
    else:
        return -1

# For example, given X = 5 and the following array A:
A = [None]*9
A[0] = 1
A[1] = 2
A[2] = 5
A[3] = 1
A[4] = 1
A[5] = 2
A[6] = 3
A[7] = 5
A[8] = 1

print("\n Solution: ", solution(A, 5))