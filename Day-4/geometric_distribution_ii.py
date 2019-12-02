result = 0
data = list(map(int, input().split()))
n = int(input())
p = data[0] / data[1]

q = 1 - p

print(round(sum([q ** (n - x) * p for x in range(1, 6)]), 3))