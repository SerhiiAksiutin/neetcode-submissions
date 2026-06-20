class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        sub = collections.defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[c][r] == ".":
                    continue
                if board[c][r] in col[c] or \
                   board[c][r] in row[r] or \
                   board[c][r] in sub[(c // 3, r // 3)]:
                    return False

                col[c].add(board[c][r])
                row[r].add(board[c][r])
                sub[(c // 3, r // 3)].add(board[c][r])

        return True
