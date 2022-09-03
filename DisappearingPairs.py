'''
https://app.codility.com/programmers/trainings/4/disappearing_pairs/
A string S containing only the letters "A", "B" and "C" is given. The string can be transformed by removing one occurrence of "AA", "BB" or "CC".

Transformation of the string is the process of removing letters from it, based on the rules described above. As long as at least one rule can be applied, the process should be repeated. If more than one rule can be used, any one of them could be chosen.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns any string that can result from a sequence of transformations as described above.
'''

def solution(S):
    orig = S
    def remove_pair(S, pair):
        splits = S.split(pair)
        return "".join(splits)
    new = remove_pair(orig, "AA")
    new = remove_pair(new, "BB")
    new = remove_pair(new, "CC")
    loop = new
    while True:
        new = remove_pair(loop, "AA")
        new = remove_pair(new, "BB")
        new = remove_pair(new, "CC")
        if not new:
            return ""
        if loop==new:
            return new
        loop = new

S = "ACCAABBC"
print("\n String: ", S)
print("\n Solution: ", solution(S))

S = "ABCBBCBA"
print("\n String: ", S)
print("\n Solution: ", solution(S))

S = "BABABA"
print("\n String: ", S)
print("\n Solution: ", solution(S))

