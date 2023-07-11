from math import factorial, exp
miu = float(input())
x = int(input())
poisson = ((miu ** x) * exp(-miu)) / factorial(x)
print("%.3f" % poisson)
