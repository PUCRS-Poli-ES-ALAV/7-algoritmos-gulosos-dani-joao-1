#2
from decimal import Decimal

"""
def escalation2(s,f,n):
    x = {}
    i = 1
    while i <= n:
        x = x + {i}
        k = i + 1
        while k <= n and s[k] < f[i]:
            k = k + 1
        i = k
    return x
"""

def escalation3(s, f, n):
    f[0] = Decimal('-Infinity')
    x = []
    i = 0

    for k in range(1,n):
        if s[k] > f[i]:
            x = x + [k]
            i = k
    return x

#print(escalation2([4,6,13,4,2,6,7,9,1,3,9], [8,7,14,5,4,9,10,11,6,13,12],4))
print(escalation3([4,6,13,4,2,6,7,9,1,3,9], [8,7,14,5,4,9,10,11,6,13,12],10))