import math

values = list(map(float, input().split()))
mean = values[0]
std = values[1]
prob_1st = float(input())
threshold = float(input())


def c_probability(mean, std, x):
    return 0.5 + 0.5 * math.erf((x - mean) / (std * (2 ** 0.5)))


print (round((1 - c_probability(mean, std, prob_1st)) * 100, 2))
print (round((1 - c_probability(mean, std, threshold)) * 100, 2))
print (round((c_probability(mean, std, threshold)) * 100, 2))
