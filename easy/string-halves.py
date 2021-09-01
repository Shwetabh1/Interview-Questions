'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        string_length = len(s)
        first_half =  string_length // 2
        second_half = first_half
        first_count, second_count, i = 0, 0, 0
        dict_vowels = {'a':1, 'e':1,'i':1,'o':1,'u':1, 'A':1, 'E':1, 'I':1, 'O':1,'U':1}
        while(i < first_half):
            if (dict_vowels.get(s[i], None)):
                first_count += 1
            if dict_vowels.get(s[second_half], None):
                second_count += 1
            i += 1
            second_half += 1
                
        return first_count == second_count