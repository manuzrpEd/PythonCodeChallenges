import datetime

### Numbers

a=35

#worst
print("\n inefficient recursive function as defined")
#because each number being calculated must also calculate for every number below it. 
def rec_fib(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
start_time = datetime.datetime.now()
for i in range(a):
    print(i, rec_fib(i))
end_time=datetime.datetime.now()
print(end_time - start_time)


#best
def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)

start_time = datetime.datetime.now()
for index, fibonacci_number in zip(range(a), fib()):
      print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
end_time=datetime.datetime.now()
print(end_time - start_time)

#second best?
print("\n efficiently memoized recursive function")
# Memoization is a method used to store the results of previous function calls to speed up future calculations.
start_time = datetime.datetime.now()
def mem_fib(n, _cache={}):
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n
for i in range(a):
    print(i, mem_fib(i))
end_time=datetime.datetime.now()
print(end_time - start_time)

### Lists:
# a=90000
# a=20

print("\n good for a list, but uses memory, maybe worse, but both very similar")
def fib_to(n):
    #recursive
     fibs = [0, 1]
     for i in range(2, n):
         fibs.append(fibs[-1] + fibs[-2])
     return fibs
start_time = datetime.datetime.now()
fib_to(a)
end_time=datetime.datetime.now()
print(end_time - start_time)

print("\n efficient (yield, generator) list of fibonacci numbers")
def fib(n):
    a, b = 0, 1
    for _ in range(n):#underscore means the value of _ is not important and not stored
        yield a #generator does generate values on the fly, not stored in memory
        a, b = b, a + b
start_time = datetime.datetime.now()
# print(list(fib(a)))
list(fib(a))
end_time=datetime.datetime.now()
print(end_time - start_time)

print("\n efficient n fibonacci number")
def fib(n):
    a, b = 0, 1
    for _ in range(n):#underscore means the value of _ is not important and not stored
        a, b = b, a + b
    return a
start_time = datetime.datetime.now()
fib(a)
end_time=datetime.datetime.now()
print(end_time - start_time)