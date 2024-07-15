"""217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time complexity O(n)

        Space complexity O(n)
        """

        # hashset = set()

        # for n in nums:

        #     if n in hashset:
        #         return True

        #     hashset.add(n)

        # return False

        ###########################
        # more pythonic way

        hashset = set(nums)

        return len(nums) != len(hashset)
