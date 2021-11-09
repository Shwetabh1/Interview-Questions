'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range, then return 0.

Example 1:
Input: num = 100
Output: 1

Example 2:
Input: num = -298
Output: 892

Example 3:
Input: num = 987
Output: 789
'''

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        while x:
            result = result * 10 + x % 10
            x //= 10

        return 0 if result > pow(2, 31) else result * symbol