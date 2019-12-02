size = int(input())
arr = list(map(int, input().split()))
weights = list(map(int, input().split()))
weighted = 0
for i in range(size):
    weighted += arr[i] * weights[i]
m_w = weighted / sum(weights)
print(round(m_w,1))