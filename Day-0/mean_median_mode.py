size = int(input())
arr = list(map(int, input().split()))

def mean(array):
    return sum(array) / len(array)

def median(array):
    size = len(array)
    array.sort()
    if size % 2 == 0:
        median = (array[(size//2)-1] + array[size//2]) / 2
        return median
    else: return array[size//2]

def mode(array):
    max = 0
    res = array[0]
    for i in array:
        freq = array.count(i)
        if freq > max:
            max = freq
            res = i
    return res

print(mean(arr))
print(median(arr))
print(mode(arr))
