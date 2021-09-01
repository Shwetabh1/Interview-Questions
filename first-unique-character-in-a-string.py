'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [0 for i in range(26)]
        for i in range(len(s)):
            arr[ord(s[i])-97] += 1
        
        answer = -1
        for i in range(len(s)):
            if arr[ord(s[i])-97] == 1:
                return i
        return answer