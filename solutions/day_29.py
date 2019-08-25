
def matrix_spiral_print(M):
        k = 0
        l = 0

        row = len(M)
        column = len(M[0])

        while (k < row and l < column):
                for i in range(l, column):
                        print(M[k][i])
                k += 1

                for i in range(k, row):
                        print(M[i][column - 1])
                column -= 1

                if (k < row):

                        for i in range(column - 1, (l - 1), -1):
                                print(M[row - 1][i])
                        row -= 1

                if (l < column):
                        for i in range(row - 1, k - 1, -1):
                                print(M[i][l])
                        l += 1

grid = [[1,  2,  3,  4,  5],
[6,  7,  8,  9,  10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12