'''
A is a list with the order of N participants
S is a string, as many characters as participants

0 player starts, sending S[0] to A[0]
Then A[0] sends S[1] to A[1] until A[N] =0
'''

def solution(S, A):
    # write your code in Python 3.6
    prev=0
    s=''
    for _ in range(0,len(S)):
        s=s+S[prev]
        prev=A[prev]
        if prev==0:
            break
    return s
    pass

S="bytdag"
A=[4,3,0,1,2,5]
# S="cdeo"
# A=[3,2,0,1]
# S="cdeenetpi"
# A=[5,2,0,1,6,4,8,3,7]
print(solution(S,A))