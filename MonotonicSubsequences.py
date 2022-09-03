# Given a sequence, find the longest subsequence that can be decomposed into at most three monotonic parts.
# change direction at most two times during your ride.
# You would like to know the maximum number of gates that you can pass with at most two changes of direction.
# https://app.codility.com/programmers/trainings/1/slalom_skiing/

# Array length is length of all numbers
# Array value is a checkpoint barrier.
# Goal is to maximise checkpoint barriers achieved with at most 2 turns (change of direction)
# hence one wants to idetify the longest monotonic subsequences.
# You want to ski to the left at the beginning.

A = [None]*13
A[0] = 15
A[1] = 13
A[2] = 5
A[3] = 7
A[4] = 4
A[5] = 10
A[6] = 12
A[7] = 8
A[8] = 2
A[9] = 11
A[10] = 6
A[11] = 9
A[12] = 3

'''
Write a function:
    def solution(A)
that, given an array A consisting of N integers, describing the positions of the gates on the track, 
returns the maximum number of gates that you can pass during one ski run.
For example, given the above data, the function should return 8, as explained above.
'''
from copy import deepcopy
def solution(A):
    assert type(A) is list
    if A == []:
        return 0
    elif len(A)==1:
        return 1
    # break down subsequences:
    lsubsequences = []
    rsubsequences = []
    # start with numbers
    for n in range(len(A)):
        lsubsequences.append([])
        rsubsequences.append([])
        # subsequences
        for s in range(n, len(A)):
            if A[s] <= A[n]:
                lsubsequences[n].append(s)
            if A[s] >= A[n]:
                rsubsequences[n].append(s)
    #     You want to ski to the left at the beginning.
    maximal_rsubseq = []
    maximal_lsubseq = []
    rsubsequences_copy = deepcopy(rsubsequences)
    lsubsequences_copy = deepcopy(lsubsequences)
    # right
    for n in range(len(rsubsequences)):
        maximal_rsubseq.append([])
        if len(rsubsequences[n]) >= 2:
            while True:
                if len(rsubsequences_copy[n]) > 1:
                    values = [A[rsubsequences_copy[n][i]] for i in range(len(rsubsequences_copy[n]))]
                    max_lst = max(values)
                    for r in range(len(rsubsequences_copy[n])):
                        value = A[rsubsequences_copy[n][r]]
                        if value == max_lst:
                            seq = rsubsequences_copy[n][0:r + 1]
                            cnt = 0
                            seq_copy = deepcopy(seq)
                            while True:
                                for s in range(1, len(seq_copy)):
                                    after = A[seq_copy[s]]
                                    before = A[seq_copy[s - 1]]
                                    if after < before:
                                        seq_copy.pop(s)
                                        break
                                cnt += 1
                                if cnt > len(values):
                                    seq = seq_copy
                                    break
                            maximal_rsubseq[n].append(seq)
                            rsubsequences_copy[n].pop(r)
                            break
                else:
                    break
        else:
            maximal_rsubseq[n].append(rsubsequences_copy[n])
    # left
    for n in range(len(lsubsequences)):
        maximal_lsubseq.append([])
        if len(lsubsequences[n]) >= 2:
            while True:
                if len(lsubsequences_copy[n]) > 1:
                    values = [A[lsubsequences_copy[n][i]] for i in range(len(lsubsequences_copy[n]))]
                    min_lst = min(values)
                    for r in range(len(lsubsequences_copy[n])):
                        value = A[lsubsequences_copy[n][r]]
                        if value == min_lst:
                            seq = lsubsequences_copy[n][0:r + 1]
                            cnt = 0
                            seq_copy = deepcopy(seq)
                            while True:
                                for s in range(1, len(seq_copy)):
                                    after = A[seq_copy[s]]
                                    before = A[seq_copy[s - 1]]
                                    if after > before:
                                        seq_copy.pop(s)
                                        break
                                cnt += 1
                                if cnt > len(values):
                                    seq = seq_copy
                                    break
                            maximal_lsubseq[n].append(seq)
                            lsubsequences_copy[n].pop(r)
                            break
                else:
                    break
        else:
            maximal_lsubseq[n].append(lsubsequences_copy[n])
    # match a left to a right and to a left
    left = [item for sublist in maximal_lsubseq for item in sublist]
    right = [item for sublist in maximal_rsubseq for item in sublist]

    list_len = [len(i) for i in left]
    max_length_left = max(list_len)
    # list_len = [len(i) for i in right]
    # max_length_right = max(list_len)

    matches = []
    if max_length_left > 1:
        for l in left:
            for r in right:
                if (len(r)>1) and (r[-1] < l[0]):
                    matches.append(r + l)
        left = matches
        final_matches = []
        for l in left:
            for r in right:
                if (len(r)>1) and (r[0] > l[-1]):
                    final_matches.append(l + r)
        # obtain the one with maximum lenght
        list_len = [len(i) for i in final_matches]
        max_length = max(list_len)
        print("\n Maximum Length: ", max_length)
        print("\n Maximum Length List: ", final_matches[list_len.index(max_length)])
        # return length of the maximum:
        return max_length
    else:
        list_len = [len(i) for i in right]
        max_length = max(list_len)
        print("\n Maximum Length: ", max_length)
        print("\n Maximum Length List: ", right[list_len.index(max_length)])
        # return length of the maximum:
        return max_length

# print(solution(A))

A = [None]*2
A[0] = 1
A[1] = 5
print(solution(A))