class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        targetRow = -1

        for i in range(rows):
            if target <= matrix[i][cols-1]:
                targetRow = i
                break
        
        for i in range(cols):
            if target == matrix[targetRow][i]:
                return True
        
        return False