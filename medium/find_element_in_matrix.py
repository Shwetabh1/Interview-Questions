Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from top to bottom.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_len = len(matrix) - 1
        
        if row_len == -1:
            return -1, -1
        
        col_len = len(matrix[0]) - 1
        
        sr = 0
        sc = col_len
        while(sr <= row_len and sc >= 0):
            if matrix[sr][sc] == target:
                return True
            elif target > matrix[sr][sc]:
                sr += 1
            else:
                sc -= 1
        
        return False

Software Engineer III

Multintional retil chain, operating discount departments, stores in more than

12
