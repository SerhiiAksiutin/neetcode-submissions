class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.sum_col = [0] * n
        self.sum_row = [0] * n
        self.main = 0
        self.anti = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        # Update
        value = 1 if player == 1 else -1
        self.sum_col[col] += value
        self.sum_row[row] += value
        if row + col == self.n - 1:
            self.anti += value
        if row == col:
            self.main += value

        # Check
        results = (self.sum_col[col], self.sum_row[row], self.anti, self.main)
        for resut in results:
            if resut == self.n or resut == -self.n:
                return player
        return 0        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
