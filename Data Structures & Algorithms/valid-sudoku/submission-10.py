class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        cel = collections.defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[c][r] == ".":
                    continue
                if board[c][r] in col[c] or \
                   board[c][r] in row[r] or \
                   board[c][r] in cel[tuple([c // 3, r // 3])]:
                       return False
                else:
                    col[c].add(board[c][r])
                    row[r].add(board[c][r])
                    cel[tuple([c // 3, r // 3])].add(board[c][r])
        return True
        