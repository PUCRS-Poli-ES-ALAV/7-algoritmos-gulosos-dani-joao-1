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

def escalation3(sf):
    n = len(sf)
    sf = list(sorted(sf.items(), key=lambda item: item[1]))

    X = []
    i = 0
    for k in range(n):
        if sf[k][0] > sf[i][1]:
            X.append(sf[k])
            i = k
    
    return X
    

#print(escalation2([4,6,13,4,2,6,7,9,1,3,9], [8,7,14,5,4,9,10,11,6,13,12],4))
print(escalation3({4:8,6:7,13:14,4:5,2:4,6:9,7:10,9:11,1:6,3:13,9:12}))