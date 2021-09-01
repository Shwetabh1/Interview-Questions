/*** 
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4. 
*/



/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var arr = [];

var createNodeArray = function (r) {
    if (r) {
    createNodeArray(r.left);    
    arr.push(r.val);
    createNodeArray(r.right);
    }
}

var checkArr = function() {
    console.log(arr);
    let ans = arr[0];
    let val = false;
    for (let i=1; i<arr.length; i++) {
        if ( ans >= arr[i] ) {
            val = true;
            break;
        }
        ans = arr[i]
    }
    if (val) {
        return false
    } else {
        return true;
    }
}

var isValidBST = function(root) {
    arr = [];
    createNodeArray(root);
     return checkArr();
   
};