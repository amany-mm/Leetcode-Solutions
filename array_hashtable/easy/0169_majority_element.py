"""
169. Majority Element
https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List

# Hash map to save number of occurrence , key: value-> n : counter
# Time complexity O(n), Space complexity -> O(n)

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}
#         res, max_count = 0, 0

#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#             res = n if count[n] > max_count else res
#             max_count = max(count[n], max_count)

#         return res


# Get rid of Hash map , no memory used, Boyer-Moore algorithm
# Time complexity O(n), Space complexity -> O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)

        return res
