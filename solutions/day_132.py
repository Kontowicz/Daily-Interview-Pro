def validate_sudoku(board):
    def check_rows(board):
        for row in board:
            tmp_row = [x for x in row if x != ' ']

            if len(set(tmp_row)) != len(tmp_row):
                return False

        return True

    def check_collumns(board):
        return check_rows(list(zip(*reversed(board))))

    def check(board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cell = []
                for tmp_i in range(i, i+3):
                    for tmp_j in range(j, j+3):
                        if board[tmp_i][tmp_j] != ' ':
                            cell.append(board[tmp_i][tmp_j])
                if len(set(cell)) != len(cell):
                    return False

        return True

    return check(board) and check_rows(board) and check_collumns(board)

board = [
    [5, ' ', 4, 6, 7, 8, 9, 1, 2],
    [6, ' ', 2, 1, 9, 5, 3, 4, 8],
    [1,   9, 8, 3, 4, 2, 5, 6, 7],
    [8,   5, 9, 7, 6, 1, 4, 2, 3],
    [4,   2, 6, 8, 5, 3, 7, 9, 1],
    [7,   1, 3, 9, 2, 4, 8, 5, 6],
    [9,   6, 1, 5, 3, 7, 2, 8, 4],
    [2,   8, 7, 4, 1, 9, 6, 3, 5],
    [3,   4, 5, 2, 8, 6, 1, 7, 9],
]

assert validate_sudoku(board) == True
print(validate_sudoku(board))
print('Test pass.')