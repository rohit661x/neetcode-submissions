class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) #init rows of input matrix

        cols = len(matrix[0]) #init cols of input matrix

        left = 0 #init left pointer at start of sorted matrix
        
        right = rows * cols - 1 #init right pointer at the end of sorted matrix

        while left <= right : #halving loop on search area
            mid = (left + right) // 2 
            #define mid index, floor division

            row = mid // cols

            col = mid % cols # col = remainder of mid / cols

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1 #search the larger value half

            else: # value > target
                right = mid - 1 #search the smaller value half

        return False 




