#2
global iter

def escalation3(sf):
    global iter
    iter = 0

    n = len(sf)
    sf = list(sorted(sf, key=lambda x: x[1]))
    X = [sf[0]]
    i = 0
    for k in range(1, n):
        iter += 1
        if sf[k][0] > sf[i][1]:
            X.append(sf[k])
            i = k
    
    return X
    
input = [(2, 4), (4, 5), (1, 6), (6, 9), (7, 10), (9, 12), (3, 13), (13, 14), (4,8), (6,7), (9,11)]
output = escalation3(input)
print("output:",output)
print("iter:",iter)