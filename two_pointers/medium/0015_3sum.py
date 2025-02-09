"""
15. 3Sum
https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Using two pointers technique
        Time complexity: O(n^2) 
        => sorting O(nlogn(n)) + two loops  O(n^2) [Outer loop + inside loop 2 pointers]

        Space complexity: O(log n) to O(n) depending on the implementation of the sorting algorithm
        """
        res = []
        nums.sort()  # sort to be easier to select the numbers (-ve to +ve)

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            # The number is equal to prev
            if i > 0 and a == nums[i - 1]:
                continue

            # After we selected the 1st number(-ve), we will select
            # the remaining two numbers using 2 pointers technique,
            # the same logic of problem 167. Two Sum II - Input Array Is Sorted
            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    # Skip the same numbers e.g [-1, -1, 2]
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
