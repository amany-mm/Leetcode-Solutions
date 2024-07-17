"""
704. Binary Search
https://leetcode.com/problems/binary-search/description/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time complexity O(log n)
        Space complexity O(1)
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return -1
