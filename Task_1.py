more = [x+1 for x in [1,2,3,4]]
# Iteration 1: x=1, x+1=2, more = [2]
# Iteration 2: x=2, x+1=3, more = [2,3]
# Iteration 3: x=3, x+1=4, more = [2,3,4]
# Iteration 4: x=4, x+1=5, more = [2,3,4,5]
print(more)


def square(n):
    return n*n

squares = [square(x) for x in [1,2,3,4]]
# Iteration 1: x=1, square(x)=1, squares = [1]
# Iteration 2: x=2, square(x)=4, squares = [1,4]
# Iteration 3: x=3, square(x)=9, squares = [1,4,9]
# Iteration 4: x=4, square(x)=16, squares = [1,4,9,16]
print(squares)


def check(n):
    return n>2

answer = [x for x in range(5) if check(x)]
# Iteration 1: x=0, check(x) is False
# Iteration 2: x=1, check(x) is False
# Iteration 3: x=2, check(x) is False
# Iteration 4: x=3, check(x) is True, answer = [3]
# Iteration 5: x=4, check(x) is True, answer = [3,4]
print(answer)


def inc(m):
    return m+1

def check(n):
    return n>2

answer = [inc(x) for x in range(5) if check(x)]
# Iteration 1: x=0, check(x) is False
# Iteration 2: x=1, check(x) is False
# Iteration 3: x=2, check(x) is False
# Iteration 4: x=3, check(x) is True, inc(x)=4, answer = [4]
# Iteration 5: x=4, check(x) is True, inc(x)=5, answer = [4,5]
print(answer)