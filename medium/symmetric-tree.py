'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

            1
    2               2
3       4       4       3

Input: root = [1,2,2,null,3,null,3]
Output: false
'''

def isSymmetric(self, root):
    def isSym(L,R):
        if L and R and L.val == R.val: 
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return L == R
    return not root or isSym(root.left, root.right)