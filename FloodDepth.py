'''
FloodDepth
Find the maximum depth of water in mountains after a huge rainfall.
https://app.codility.com/programmers/trainings/1/flood_depth/

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the maximum depth of water.
'''

# Example:
A = [0]*11
A[0] = 1
A[1] = 3
A[2] = 2
A[3] = 1
A[4] = 2
A[5] = 1
A[6] = 5
A[7] = 3
A[8] = 3
A[9] = 4
A[10] = 2

print("\n Array: ", A)
# Given array A shown above, the function should return 2, as explained above, the maximum water depth of this area is 2.

def flood_depth(A):
    depth = [0]*len(A)
    peaks = []

    if len(A)<=2:
        return 0
    # identfy peaks:
    for p in range(len(A)-1):
        if (p < len(A)) and (A[p] > A[p + 1]) and (A[p] > A[p - 1]):
            peaks.append(p)
    if peaks == []:
        return 0
    if len(peaks) <= 1:
        return 0
    # remove flooded peaks:
    above_water_peaks = peaks.copy()
    for p in range(1, len(peaks)-1):
        if (A[peaks[p]] < A[peaks[p-1]]) and  (A[peaks[p]] < A[peaks[p+1]]):
            above_water_peaks.remove(peaks[p])
    # define depth:
    for p in range(len(A)):
        if (p <= above_water_peaks[0]) or (p >= above_water_peaks[-1]):
            continue
        for q in range(len(above_water_peaks)):
            if (p > above_water_peaks[q]) and (p < above_water_peaks[q+1]):
                min_lake = min(A[above_water_peaks[q]], A[above_water_peaks[q+1]])
                break
        depth[p] = min_lake - A[p]

    return max(depth)

max_depth = flood_depth(A)

print("\n Max. depth: ", max_depth)

# For the following array:
#     A[0] = 5
#     A[1] = 8
#
# the function should return 0, because this landscape cannot hold any water.
A = [0]*2
A[0] = 5
A[1] = 8
max_depth = flood_depth(A)
print("\n Max. depth: ", max_depth)

A = [0]*3
A[0] = 5
A[1] = 8
A[2] = 16
max_depth = flood_depth(A)
print("\n Max. depth: ", max_depth)

A = [0]*4
A[0] = 5
A[1] = 8
A[2] = 16
A[3] = 10
max_depth = flood_depth(A)
print("\n Max. depth: ", max_depth)


