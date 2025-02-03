"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Using prefix sum concept
        Time complexity O(n)
        Space complexity O(n)
        """
        count_subarrays = 0
        sum_ = 0
        sum_counter = {0: 1}

        for num in nums:
            sum_ += num

            count_subarrays += sum_counter.get(sum_ - k, 0)

            sum_counter[sum_] = sum_counter.get(sum_, 0) + 1

        return count_subarrays
