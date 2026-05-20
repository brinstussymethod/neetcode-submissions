class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix) , len(matrix[0])
        top, bot = 0 , ROWS - 1 
        #check where the value could be in rows
        while top <= bot:
            row = (top + bot) // 2 
            if (target > matrix[row][-1]):
                top = row + 1 
            elif target < matrix[row][0]:
                bot = row - 1 
            else:
                break 
        
        
        #none of the rows contain the target value out of bounds

        if not (top <= bot):
            return False 
        #check where value could be in the column
        row = (top + bot) // 2 
        l, r = 0 , COLS - 1 
        while l <= r:
            m = (l + r) // 2 
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True 
        return False 

        
        

