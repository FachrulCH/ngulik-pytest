# Given a non-negative integer, return an array / a list of the individual digits in order.
# Examples:
# 123 => [1,2,3]
# 1 => [1]
# 8675309 => [8,6,7,5,3,0,9]
# Solution

def digitize(num):
    arr = []
    numbers = list(str(num))
    for n in numbers:
        arr.append(int(n))
    return arr

print(digitize(12))