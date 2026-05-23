class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        hash_row = defaultdict(list)
        hash_col = defaultdict(list)
        hash_sq = defaultdict(list)

        for i in range(rows):
            for j in range(cols):
                if (board[i][j] == '.'):
                    continue
                if (board[i][j] in hash_row[i] or 
                    board[i][j] in hash_col[j] or 
                    board[i][j] in hash_sq[(i//3, j//3)]):
                    return False
                
                hash_row[i].append(board[i][j])
                hash_col[j].append(board[i][j])
                hash_sq[(i//3, j//3)].append(board[i][j])
        
        return True