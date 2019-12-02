# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else: return factorial(n - 1) * n

mean = float(input())
k = float(input())
e = 2.71828

P = ((mean ** k) * (e**-mean)) / factorial(k)
print(round(P, 3))
