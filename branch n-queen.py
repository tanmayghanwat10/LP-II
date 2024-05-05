import copy
n = int(input("Board Dimensions: "))
board = [["-" for i in range(n)] for j in range(n)]

slash = copy.deepcopy(board)
r_slash = copy.deepcopy(board)

for i in range(n):
    for j in range(n):
        slash[i][j] = i+j
        r_slash[i][j] = i-j+(n-1)
used_row = []
used_dia = []
used_rdia = []

def helper(j):
    if j == n:
       return True
     
    for i in range(n):
        if i in used_row or slash[i][j] in used_dia or r_slash[i][j] in used_rdia:
            pass
        else:
            board[i][j] ="Q"
            used_row.append(i)
            used_dia.append(slash[i][j])
            used_rdia.append(r_slash[i][j])
            check = helper(j+1)
            if check:
                return True
            board[i][j] = "-"
            used_row.remove(i)
            used_dia.remove(slash[i][j])
            used_rdia.remove(r_slash[i][j])
    return False

helper(0)
for i in board:
    for j in i:
        print(j, end= " ")
    print()

