class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        squ = defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in col[c] or \
                   board[r][c] in row[r] or \
                   board[r][c] in squ[tuple([c // 3, r // 3])]:
                   return False
                else:
                    col[c].add(board[r][c])
                    row[r].add(board[r][c])
                    squ[tuple([c // 3, r // 3])].add(board[r][c])
        return True
        