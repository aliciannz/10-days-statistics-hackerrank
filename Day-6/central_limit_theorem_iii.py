import math
n = float(input())
mean = float(input())
std = float(input())
distr = float(input())
z = float(input())
print(round(mean - (std / (n**0.5))* z, 2))
print(round(mean + (std / (n**0.5))* z, 2))
