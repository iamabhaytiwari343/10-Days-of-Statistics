import math
def binomial_prob(n, p, x):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x))) * \
        (p**x)*((1-p)**(n-x))
    return (b)
reject_percent, n = map(float, '12 10'.split())
p = reject_percent/100
b = 0
for x in range(0, 3):  # x=0,1,2
    b += binomial_prob(n, p, x)
print("%.3f" % b)
print(round(sum([binomial_prob(n, p, i)
      for i in range(2, 11)]), 3))  # x=2,3,4,...,10
