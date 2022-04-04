# 1
global iter

def exchange(input, available):
    global iter
    iter = 0
    available.sort(reverse=True)
    exchange = dict((e,0) for e in available)

    for coin in available:
        while(input > coin):
            iter += 1
            input -= coin
            exchange[coin] += 1
            
    return exchange

print(exchange(389, [100,25,50,10,5,1]), f"\n{iter = }")

