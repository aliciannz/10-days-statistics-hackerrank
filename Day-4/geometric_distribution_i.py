data = list(map(int, input().split()))
n = int(input())
p = data[0] / data[1]

q = 1 - p
print(round(q ** (n - 1) * p, 3))