def fact(n):
    if n == 1 or n==0:
        return 1
    else:
        return fact(n-1) * n

def b(x,n,p):
    return fact(n) / (fact(x) * fact(n-x)) * p**x * (1-p)**(n-x)

data = list(map(float, input().split()))
p = (data[0] / 100)
n = int(data[1])

print(round(sum([b(i, n, p) for i in range(0, 3)]), 3))
print(round(sum([b(i, n, p) for i in range(2, n+1)]), 3))
