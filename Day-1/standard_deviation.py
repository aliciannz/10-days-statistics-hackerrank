
import math
def mean(arr):
    return sum(arr) / len(arr)

def stddev(arr):
    total = 0
    for i in range(size):
        total = total + (arr[i] - mean(arr)) ** 2
    return math.sqrt(total / size)

size = int(input())
arr = list(map(int, input().split()))
sigma = stddev(arr)
print(round(sigma,1))