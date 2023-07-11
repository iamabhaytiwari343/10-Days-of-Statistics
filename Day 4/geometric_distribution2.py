def geometric_prob(p, x):
    g = (1-p)**(x-1) * p
    return(g)
numerator, denominator = map(float, input().split())
x = int(input())
p = numerator/denominator
g = 0
for i in range(1,6):
    g += geometric_prob(p, i)   
print("%.3f" %g)