def median(array):
    size = len(array)
    array.sort()
    if size % 2 == 0:
        median = (array[(size // 2) - 1] + array[size // 2]) / 2
        return median
    else:
        return float(array[size // 2])
#
size = int(input())
arr = list(map(int, input().split()))
freq = list(map(int, input().split()))

#
new_arr = list()
for i in range(len(arr)):
    for j in range(freq[i]):
        new_arr.append(arr[i])
new_arr.sort()
size = int(len(new_arr))


L = new_arr[:size // 2]
if size % 2 == 0:
    U = new_arr[size // 2:]
else:
    U = new_arr[(size // 2) + 1:]

Q_1 = median(L)
Q_3 = median(U)

print(Q_3-Q_1)
