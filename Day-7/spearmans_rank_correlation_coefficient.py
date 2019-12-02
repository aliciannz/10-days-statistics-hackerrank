n = int(float(input()))
x = list(map(float, input().split()))
y = list(map(float, input().split()))


def rank(x):
    rx = [sorted(x).index(i) for i in x]
    return rx


rx = rank(x)
ry = rank(y)
d = [(rx[i] - ry[i]) ** 2 for i in range(n)]
r_xy = 1 - (6 * sum(d)) / (n * (n ** 2 - 1))
print(round(r_xy, 3))
