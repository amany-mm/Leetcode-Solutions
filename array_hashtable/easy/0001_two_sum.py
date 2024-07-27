"""1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time complexity O(n)
        Space complexity O(n)

        """
        prev_map = {}  # value: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prev_map:
                return [prev_map[diff], i]

            prev_map[n] = i
