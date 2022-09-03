def quick_sort(s):
    if len(s) == 1 or len(s) == 0:
       return s
    else:
        pivot = s[0]
        i = 0
        for j in range(len(s)-1):
            if s[j+1] < pivot:
               s[j+1],s[i+1] = s[i+1],s[j+1]
               i += 1
        s[0],s[i] = s[i],s[0]
        # recursive
        first_part = quick_sort(s[:i])
        second_part = quick_sort(s[i+1:])
        first_part.append(s[i])
        return first_part + second_part
my_list = [64,25,83,47,67,14]
quick_sort(my_list)
print(my_list)