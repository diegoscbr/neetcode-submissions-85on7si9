class Solution:
    def binSearch(self, row, target):
        start = 0
        end = len(row) - 1
        while end >= start:
            m = start + (end - start) // 2
            if target == row[m]:
                return True
            elif target > row[m]:
                start = m+1
            elif target < row[m]:
                end = m - 1
        return False
        
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            #do bin Search
            
            if self.binSearch(row, target) == True:
                return True
        return False
