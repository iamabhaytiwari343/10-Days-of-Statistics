import math

def binomial_prob(n, p, x):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

boy, girl = map(float, input().split())
n = 6
p = boy/(boy+girl)
b = 0
for x in range(3,7): # x=3,4,5,6
    b += binomial_prob(n, p, x)   
print("%.3f" %b)