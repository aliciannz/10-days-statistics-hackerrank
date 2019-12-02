# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics 
n = int(float(input()))
x = list(map(float, input().split()))
y = list(map(float, input().split()))

def pcc(x,y,n):
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    std_x = statistics.pstdev(x)
    std_y = statistics.pstdev(y)

    cov =  sum([(x[i] - mean_x) * (y[i] -mean_y) for i in range(n)])
    p_xy = cov / (n* std_x * std_y)
    return p_xy
    
print (round(pcc(x,y,n), 3))
