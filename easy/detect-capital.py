'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
'''

class Solution:
    
    def allUpper(self,str):
        for char in str:
            ascii_code = ord(char)
            if ascii_code <65 or ascii_code >90:
                return False
        print('returning true')
        return True
    
    def allLower(self,str):
        for char in str:
            ascii_code = ord(char)
            if ascii_code <97 or ascii_code >122:
                return False
        return True
       
    def detectCapitalUse(self, word: str) -> bool:
        # case when only one letter exists
        if len(word) == 1:
            return True
        # get the first capital letter
        firstCapital = word[0].isupper()
        # get the second caspital letter
        secondCapital = word[1].isupper()
        # conditions
        if firstCapital and secondCapital:
            # all others should be upper
            return self.allUpper(word[1:])
        elif firstCapital:
            return self.allLower(word[1:])
        else:
            return self.allLower(word[1:])