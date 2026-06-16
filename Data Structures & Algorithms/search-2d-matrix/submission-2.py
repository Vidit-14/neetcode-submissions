class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        rowSt = 0
        rowEn = rows - 1
        rowMid = -1
        colSt = 0
        colEn = cols - 1
        colMid = -1

        while rowSt <= rowEn:
            rowMid = (rowSt + rowEn) // 2
            if target > matrix[rowMid][cols-1]:
                rowSt = rowMid + 1
            elif target < matrix[rowMid][0]:
                rowEn = rowMid - 1
            else:
                break
        
        while colSt <= colEn:
            colMid = (colSt + colEn) // 2
            if target == matrix[rowMid][colMid]:
                return True
            elif target < matrix[rowMid][colMid]:
                colEn = colMid - 1
            else:
                colSt = colMid + 1
            
        
        return False