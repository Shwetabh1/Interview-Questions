'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if m == 1 and n == 1:
            return grid[0][0]
        
        cost_matrix = [[0] * n] * m
        cost_matrix[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    cost_matrix[i][j] = grid[i][j] + cost_matrix[i][j-1]
                elif j == 0 and i > 0:
                    cost_matrix[i][j] = grid[i][j] + cost_matrix[i-1][j]
                else:
                    cost_matrix[i][j] = min(cost_matrix[i-1][j], cost_matrix[i][j-1]) +  grid[i][j]
        print(cost_matrix)
        return cost_matrix[-1][-1]