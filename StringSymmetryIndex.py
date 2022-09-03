'''
Write a function:

    def solution(S)

that, given a string S, returns the index (counting from 0) of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. The function should return −1 if no such index exists.

Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.
'''

def solution(S):
    if S=='':
        return -1
    if len(S)==1:
        return 0
    if (len(S) % 2) == 0:
        return -1
    else:
        midpoint = int((len(S)+1)/2) - 1
        first = S[0:midpoint]
        second = S[midpoint+1:]
        second_inv = list(second)
        inverted = []
        for i in range(len(second_inv)-1,-1,-1):
            inverted.append(second_inv[i])
        inverted = "".join(inverted)
        if inverted==first:
            return midpoint
        else:
            return -1

# For example, given a string:
S = "racecar"
print("\n String: ", S)
print("\n Solution: ", solution(S))

S = "x"
print("\n String: ", S)
print("\n Solution: ", solution(S))

S = "cacutaco"
print("\n String: ", S)
print("\n Solution: ", solution(S))