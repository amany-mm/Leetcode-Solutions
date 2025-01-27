"""
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time complexity O(n)
        Space complexity O(n)
        """
        set_num1 = set(nums1)
        set_num2 = set(nums2)

        return list(set_num1 & set_num2)
