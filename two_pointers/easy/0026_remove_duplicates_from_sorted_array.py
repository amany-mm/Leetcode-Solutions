"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,
you need to do the following things:

  - Change the array nums such that the first k elements of nums contain the
  unique elements in the order they were present in nums initially.
  The remaining elements of nums are not important as well as the size of nums.
  - Return k.
  
Constraints:
  1 <= nums.length <= 3 * 104

Example 1:
  Input: nums = [1,1,2]
  Output: 2, nums = [1,2,_]
  Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
  It does not matter what you leave beyond the returned k (hence they are underscores).
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Using two pointers solution
        fast pointer always loop through array element
        Whereas slow pointer only increased in 2 special cases:
        if it's at the first element [No previous to compare with]
        or it's unique [pervious is not equal]
        Otherwise not increased to override the duplicate in the next iteration

        Time complexity O(n)
        Space complexity O(1)
        """
        slow = 0

        for fast in nums:
            if slow == 0 or fast != nums[slow - 1]:
                nums[slow] = fast

                slow += 1

        return slow
