"""
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        Using two pointers technique
        Time complexity O(n)
        Space complexity O(1)
        """
        l, r = 0, len(s) - 1

        while l < r:
            # swap 2 characters
            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1
