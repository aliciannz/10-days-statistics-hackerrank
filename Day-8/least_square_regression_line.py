x = []
y = []
import statistics
n=5
for _ in range(5):
    z = input().split()
    x.append(int(z[0]))
    y.append(int(z[1]))
mean_x = statistics.mean(x)
mean_y = statistics.mean(y)

x_sqr_sum = sum([x_i**2 for x_i in x])
xy = sum([x[i]*y[i] for i in range(5)])
b = ((n * xy) - sum(x)*sum(y))/ (n * x_sqr_sum - (sum(x) ** 2))
a = mean_y - b * mean_x
print (round(a + 80 * b, 3))