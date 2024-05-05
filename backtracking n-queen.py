import copy
n = int(input("Board Dimensions: "))
board = [["-" for i in range(n)] for j in range(n)]

def helper(j):
    if j == n:
        return True
    for i in range(n):
        skip = False
        # row check
        for x in range(j):
            if board[i][x] == "Q":
                skip = True
        # 1 diagonal
        x, y = i ,j 
        while x > -1 and y > -1:
            if board[x][y] == "Q":
                skip = True
            x -= 1
            y -= 1
        # 2 diagonal
        x, y = i, j
        while x < n and y > -1:
            if board[x][y] == "Q":
                skip = True
            x += 1
            y -= 1
        if skip:
            pass
        else:
            board[i][j] = "Q"
            if helper(j+1):
                return True
            board[i][j] = "-"
    return False

helper(0)
for i in board:
    for j in i:
        print(j, end= " ")
    print()