from math import factorial

def Combinations(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

count = 0

for n in range(1,101):
    for r in range(1,n+1):
        if(Combinations(n,r) > 1000000):
            count += 1

print "The number of combinations greater than 1000000 is %d" % count
