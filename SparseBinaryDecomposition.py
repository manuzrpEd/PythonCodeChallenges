# Decompose int into sum of ints having no consecutive 1s in binary form.

# integer to bit
def int_to_bit(N: int):
    return format(N, 'b')

def binary_gap(N):
    print("Number:",N)
    print("Binary Number:,",format(N, 'b'))
    return len(max(format(N, 'b').strip('0').split('1')))

# list of integers that are conformable to N
def list_conformable(N: int):
    # get int in bits:
    Nbit = str(int_to_bit(N))
    # count 0s in Nbit:
    cnts = Nbit.count('0')
    # idxs of 0s:
    idxs = [i for i,v in enumerate(Nbit) if Nbit[i]=='0']
    # print(idxs)
    # list of combinations
    lst = []
    for numbers in itertools.product([0, 1], repeat=cnts):
        lst.append(numbers)
    # list of new Nbits
    Nbits = []
    for l in lst:
        s = list(Nbit)
        # print(s)
        # print(l)
        for i in range(len(idxs)):
            s[idxs[i]] = str(l[i])
        Nbits.append("".join(s))
        # Nbits.append(int("".join(s),2))
    return Nbits

# A non-negative integer N is called sparse if its binary representation does not contain two consecutive bits set to 1.
def N_sparse(N: int):
    '''
    https://www.tutorialspoint.com/check-if-a-string-has-m-consecutive-1s-or-0s-in-python
    '''
    Nbit = int_to_bit(N)
    str_size = len(Nbit)
    count_1 = 0
    for i in range(0, str_size - 1):
        if (Nbit[i] == '1'):
            count_1 += 1
        else:
            count_1 = 0
        if (count_1 == 2):
            return False
    return True

# For example, 41 is sparse, because its binary representation is "101001" and it does not contain two consecutive 1s.
N = 41
print('\n N: ', N)
print('\n int_to_bit: ', int_to_bit(N))
print('\n Sparse: ', N_sparse(N))

# On the other hand, 26 is not sparse, because its binary representation is "11010" and it contains two consecutive 1s.
N = 26
print('\n N: ', N)
print('\n int_to_bit: ', int_to_bit(N))
print('\n Sparse: ', N_sparse(N))

# Two non-negative integers P and Q are called a sparse decomposition of integer N if P and Q are sparse and N = P + Q.
def sparse_decomposition(P: int, Q: int, N: int):
    return (N_sparse(P)) and (N_sparse(Q)) and (N == P +Q)

# For example, 8 and 18 are a sparse decomposition of 26 (binary representation of 8 is "1000", binary representation of 18 is "10010");
P = 8
print('\n P: ', P)
print('\n int_to_bit: ', int_to_bit(P))
print('\n Sparse: ', N_sparse(P))
Q = 18
print('\n Q: ', Q)
print('\n int_to_bit: ', int_to_bit(Q))
print('\n Sparse: ', N_sparse(Q))
N = 26
print('\n N: ', N)
print('\n sparse_decomposition: ', sparse_decomposition(P, Q, N))

# 9 and 17 are a sparse decomposition of 26 (binary representation of 9 is "1001", binary representation of 17 is "10001");
P = 9
print('\n P: ', P)
print('\n int_to_bit: ', int_to_bit(P))
print('\n Sparse: ', N_sparse(P))
Q = 17
print('\n Q: ', Q)
print('\n int_to_bit: ', int_to_bit(Q))
print('\n Sparse: ', N_sparse(Q))
N = 26
print('\n N: ', N)
print('\n sparse_decomposition: ', sparse_decomposition(P, Q, N))

# 2 and 24 are not a sparse decomposition of 26; though 2 + 24 = 26, the binary representation of 24 is "11000", which is not sparse.
P = 2
print('\n P: ', P)
print('\n int_to_bit: ', int_to_bit(P))
print('\n Sparse: ', N_sparse(P))
Q = 24
print('\n Q: ', Q)
print('\n int_to_bit: ', int_to_bit(Q))
print('\n Sparse: ', N_sparse(Q))
N = 26
print('\n N: ', N)
print('\n sparse_decomposition: ', sparse_decomposition(P, Q, N))

'''
Write a function:

    def solution(N)

that, given a non-negative integer N, returns any integer that is one part of a sparse decomposition of N. 
The function should return −1 if there is no sparse decomposition of N.

Assumptions:
N is an integer within the range [0..1,000,000,000].
'''
def solution(N: int):
    assert N>=0
    # get P + Q combinations that add up to N
    # Use that N - P = Q, so given N, Q is a function of P and the other way around.
    P = range(0,N+1)

    for p in P:
        q = N - p
        if (N_sparse(p)) and (N_sparse(q)):
            return p
    return -1

# For example, given N = 26 the function may return 8, 9, 17 or 18, as explained in the example above.
# All other possible results for N = 26 are 5, 10, 16 and 21.
N = 26
print('\n Sparse: ', N_sparse(N))
print('\n Solution: ', solution(N))