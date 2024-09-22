"""
594. Longest Harmonious Subsequence

We define a harmonious array as an array where the difference between
its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious
subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
"""
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Using a hashmap of frequency of each element and its neighboring elements
        Time complexity: O(n)
        Space complexity: O(n)
        """
        max_length = 0
        freq = {}

        if not nums:
            return 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            if key + 1 in freq:
                current_length = value + freq[key + 1]

                max_length = max(max_length, current_length)

        return max_length
