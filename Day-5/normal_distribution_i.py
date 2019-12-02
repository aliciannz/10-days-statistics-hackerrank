import math
values = list(map(float, input().split()))
mean = values[0]
std = values[1]
prob_1st = float(input())
range_2nd = list(map(float, input().split()))

def c_probability(mean, std, x):
    return 0.5 + 0.5 * math.erf((x - mean) / (std * (2 ** 0.5)))
print (round(c_probability(mean, std, prob_1st),3))
print (round(c_probability(mean, std, range_2nd[1])-c_probability(mean, std, range_2nd[0]), 3))