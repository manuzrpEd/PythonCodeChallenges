# My solution assumes that 30-bit integers will be provided.
# A more general answer could be provided for any n-bt integers, for example
# (0, 0, 0)

import itertools

# integer to bit
def int_to_bit(N: int):
    return format(N, 'b')

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

# list of unique Nbit integers
def unique_list(lst: list):
    Ns = []
    for n in range(len(lst)):
        Ns += list_conformable(lst[n])
    return list(set(Ns))
#  only for 3, 30bits Integers:
def unique_list_three(A, B, C):
        lst = [A, B, C]
        Ns = []
        for n in range(len(lst)):
            Ns += list_conformable(lst[n])
        return list(set(Ns))
            
# print(list_conformable(1073741727))
lst = [1073741727, 1073741631, 1073741679]
print("\n Unique List: \n\n", unique_list(lst))
print("\n Length: ", len(unique_list(lst)))
#  only for 3, 30bits Integers:
# A = 1073741727
# B = 1073741631
# C = 1073741679
A = 0
B = 0
C = 0
print("\n Length Three: ", len(unique_list_three(A, B, C)))

# # check conformability for 2 integers in bites
# def conformable(N1: int, N2: int):
#     '''
#     We say that integer A conforms to integer B if, 
#     in all positions where B has bits set to 1, 
#     A has corresponding bits set to 1.
#     '''
#     if len(bin(N1)) != len(bin(N2)):
#         return False
#     a_str, b_str = str(int_to_bit(N1)), str(int_to_bit(N2))
#     idxs = [i for i,v in enumerate(b_str) if b_str[i]=='1']
#     print("\n idxs: ", idxs)
#     a_str = [a_str[i] for i in idxs]
#     b_str = [b_str[i] for i in idxs]
#     print("\n a_str: ", a_str)
#     print("\n b_str: ", b_str)
    
#     return '0' not in a_str

# # Conformable:
# N1 = 16244239
# N2 = 13032961
# print(conformable(N1,N2))

# # Not Conformable:
# N1 = 819399173
# N2 = 9843471
# print(conformable(N1,N2))

# # inefficient
# # return list of integers that are conformable to N
# def list_conformable(N: int):
#     lst = []
#     for i in range(0, 1073741823):
#         if conformable(i, N):
#             lst.append(i)
#             print(i)
# print(list_conformable(1073741727))


    