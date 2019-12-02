size = int(input())
arr = list(map(int, input().split()))
arr.sort()


def median(array):
    size = len(array)
    array.sort()
    if size % 2 == 0:
        median = (array[(size // 2) - 1] + array[size // 2]) / 2
        return int(median)
    else:
        return int(array[size // 2])


L = arr[:size // 2]
if size % 2 == 0:
    U = arr[size // 2:]
else:
    U = arr[(size // 2) + 1:]

Q_1 = median(L)
Q_2 = median(arr)
Q_3 = median(U)

print(Q_1)
print(Q_2)
print(Q_3)