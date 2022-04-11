board = [[ 0 for _ in range(7)] for _ in range(7) ]
stack = [(0,0)]

board[0][0] = 1

def isSafe(pos):
    position = pos

    for i in range(0, len(board)):
        if board[i][pos[1]]: return 0
    
    for j in range(0, len(board[0])):
        if board[pos[0]][j]: return 0
    
    while(pos[0] >= 0 and pos[1] >= 0):
        if board[pos[0]][pos[1]]: return 0
        pos[0] -= 1
        pos[1] -= 1
    

    return 1

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]: continue
        board[i][j] = isSafe([i,j])

for i in range(len(board)):
    print(board[i])