class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        cel = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in row[r]:
                    print(board[r][c])
                    print(row[r])
                    return False
                else:
                    row[r].add(board[r][c])
                
                if board[r][c] in col[c]:
                    return False
                else:
                    col[c].add(board[r][c])

                if board[r][c] in cel[(c // 3, r // 3)]:
                    return False
                else:
                    cel[(c // 3, r // 3)].add(board[r][c])
        return True
