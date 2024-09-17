"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Using 2 pointers technique, to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

        Moving all non zeros to the left more easier then move zeros to the right.
        So we have 0 value. In that case, we don't do anything. when  we find a non zero number, we swap numbers, we only move left pointer to the next.
        And then, we move right pointer to the next in the next iteration.

        Time complexity O(n)
        Space complexity O(1)
        """
        left = 0

        for right in range(len(nums)):

            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums
