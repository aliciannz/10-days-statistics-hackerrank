
import math
max_weight = float(input())
num_boxes = float(input())
mean = float(input())
std = float(input())

def c_probability(mean, std, x):
    return 0.5 + 0.5 * math.erf((x - mean) / (std * (2 ** 0.5)))
mean_sum = mean * num_boxes
std_sum = math.sqrt(num_boxes) * std
print (round(c_probability(mean_sum, std_sum, max_weight), 4))


