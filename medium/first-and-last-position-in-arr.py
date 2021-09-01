'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums) - 1
        start = 0
        end = length
        answer_1 = -1
        while start <= end:
            mid = (start + end ) // 2
            if nums[mid] == target:
                answer_1 = mid
                start = 0
                end = mid - 1 # keep looking at left
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        # reset and start again
        start = 0
        end = length
        answer_2 = -1
        while start <= end:
            mid = (start + end)// 2
            if nums[mid] == target:
                answer_2 = mid
                start = mid + 1 # keep looking at right
                end = length
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return [answer_1, answer_2]