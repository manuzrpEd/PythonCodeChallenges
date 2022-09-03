def binary_gap(N):
    print("Number:",N)
    print("Binary Number:,",format(N, 'b'))
    return len(max(format(N, 'b').strip('0').split('1')))  

# Enter Integer value
print(binary_gap(32))