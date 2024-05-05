def print_board(board):
    for i in board:
        for j in i:
            if i == 0:
                print("-", end =" ")
            print(j, end = " ")
        print()
class puzzle:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.crow = 2
        self.ccol = 2
    def create(self):
        print("'0' is the movable cursor") 
        for i in range(3):
            for j in range(3):
                val = int(input("Enter piece number:- "))
                if val == 0:
                    self.crow = i
                    self.ccol = j
                self.board[i][j] = val
        print_board(self.board)
    def move_right(self):
        if  self.ccol  == 2:
            return False
        self.board[self.crow][self.ccol], self.board[self.crow][self.ccol+1] = self.board[self.crow][self.ccol+1], self.board[self.crow][self.ccol]
        self.ccol += 1
        return True
    def move_left(self):
        if self.ccol == 0:
            return False
        self.board[self.crow][self.ccol], self.board[self.crow][self.ccol-1] = self.board[self.crow][self.ccol-1], self.board[self.crow][self.ccol]
        self.ccol -= 1
        return True
    def move_up(self):
        if self.crow == 0:
            return False
        self.board[self.crow][self.ccol], self.board[self.crow-1][self.ccol] = self.board[self.crow-1][self.ccol], self.board[self.crow][self.ccol]
        self.crow -=1 
        return True
    def move_down(self):
        if self.crow == 2:
            return False
        self.board[self.crow][self.ccol], self.board[self.crow+1][self.ccol] = self.board[self.crow+1][self.ccol], self.board[self.crow][self.ccol]
        self.crow += 1
        return True
    
    def manhattan_distance(self, goal_state):
        distance = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    tile = self.board[i][j]
                    goal_row, goal_col = (tile - 1) // 3, (tile - 1) % 3
                    distance += abs(i - goal_row) + abs(j - goal_col)

        return distance
    
    def possible_move(self):
        moves = [1,1,1,1]
        if self.crow == 0:
            moves[0] = 0
        if self.crow == 2:
            moves[1] = 0
        if self.ccol == 0:
            moves[2] = 0
        if self.ccol == 2:
            moves[3] = 0
        return moves

state = puzzle()
state.create()

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

print("solving process is like this: ")

n = 0
while state.board != goal and n < 300:
    n += 1
    possible = state.possible_move()
    u, d, l, r = float("inf"), float("inf"), float("inf"), float("inf")
    mini = float("inf")
    min_move = ""
    for index,move in enumerate(possible):
        if move:
            if index == 0:
                state.move_up()
                u = state.manhattan_distance(goal)
                if u < mini:
                    mini = u
                    min_move = "u"
                state.move_down()
            elif index == 1:
                state.move_down()
                d = state.manhattan_distance(goal)
                if d < mini:
                    mini = d
                    min_move = "d"
                state.move_up()
            elif index == 2:
                state.move_left()
                l = state.manhattan_distance(goal)
                if l < mini:
                    mini = l
                    min_move = "l"
                state.move_right()
            elif index == 3:
                state.move_right()
                r = state.manhattan_distance(goal)
                if r < mini:
                    mini = r
                    min_move = "r"
                state.move_left()
    

    if min_move == "l":
        state.move_left()
    elif min_move == "r":
        state.move_right()
    elif min_move == "u":
        state.move_up()
    elif min_move == "d":
        state.move_down()
    
    print_board(state.board)
    print()
    
    if state.board == goal:
        print(f"found answerer in: {n}")
        break

if n == 300:
    print("sorry faild to find answer")




        