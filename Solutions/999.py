class Solution:
    def numRookCaptures(self, board) -> int:
        ind_x_R = 0
        ind_y_R = 0
        ind_x_current = 0
        ind_y_current = 0
        for x, row in enumerate(board):
            for y, elem in enumerate(row):
                if elem == "R":
                    ind_x_R, ind_y_R = x, y
                    ind_x_current, ind_y_current = x, y
        # print("ind_x_R, ind_y_R : ", ind_x_R, ind_y_R)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        count = 0
        for direction in directions:
            while 0 <= ind_x_current + direction[0] <=7 and 0 <= ind_y_current + direction[1] <= 7:

                ind_x_current += direction[0]
                ind_y_current += direction[1]

                # print(ind_x_current, ind_y_current)
                if board[ind_x_current][ind_y_current] == "B":
                    break
                if board[ind_x_current][ind_y_current] == "p":
                    count += 1
                    break
            ind_x_current, ind_y_current = ind_x_R, ind_y_R
        # print(count)
        return count

board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

S = Solution()
S.numRookCaptures(board)