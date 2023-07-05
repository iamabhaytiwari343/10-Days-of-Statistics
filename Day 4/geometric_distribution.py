def geometric_prob(p, x):
    g = (1-p)**(x-1) * p
    return(g)

numerator, denominator = map(float, input().split())
x = int(input())
p = numerator/denominator
g = geometric_prob(p, x)  
print("%.3f" %g)