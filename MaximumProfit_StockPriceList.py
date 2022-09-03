"""
Let's create Spotify, finance trading problem:
find the maximum benefit of stock oscillating over time
also what start index and what end index generates such maximum benefit
"""
def solution(L):
    if isinstance(L, list):
        if len(L)>=1:
            lst=[]
            lst_end=[]
            for i in range(len(L)-1):
                initial=L[i]
                sub_lst=[]
                for j in range(i+1,len(L)):
                    sub_lst.append(L[j]-initial)
                max_value_sub=max(sub_lst)
                max_index_end=[1+i+q for q, x in enumerate(sub_lst) if x == max_value_sub]
                lst.append(max_value_sub)
                lst_end.append(max_index_end)
            max_value=max(lst)
            max_index_start=[i for i, x in enumerate(lst) if x == max_value]
            max_index_end=[lst_end[max_index_start[i]][0] for i in range(len(max_index_start))]
            return max_value,max_index_start,max_index_end
        else:
            return "empty list"
    else:
        return "Not a list"
    pass

# L=[]
# L=2
L=[2,9,8,0,4,5,7,18,-2]
print(solution(L))