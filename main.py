board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    if (searchEmptyBox(board) == None):
        return True
    [row, col] = searchEmptyBox(board)
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def verticalCheck(board, col, row, val):
    for row in range(len(board[0])):
        if (board[col][row] == val):
            return False
    return True


def horizontalCheck(board, row, val):
    for col in range(len(board[0])):
        if (board[col][row] == val):
            return False
    return True


def boxCheck(board, col, row, val):
    startcol = col // 3
    startrow = row // 3
    for i in range(startcol * 3, startcol * 3 + 3):
        for j in range(startrow * 3, startrow * 3 + 3):
            if (board[i][j] == val):
                return False
    return True


def valid(bo, num, pos):
    # Check row
    col = pos[0]
    row = pos[1]
    if (not verticalCheck(bo, col, row, num)):
        return False

    if (not horizontalCheck(bo, row, num)):
        return False

    if (not boxCheck(bo, col, row, num)):
        return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def searchEmptyBox(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if (board[col][row] == 0):
                return [col, row]
    return None


print_board(board)
solve(board)
print("___________________")
print_board(board)
