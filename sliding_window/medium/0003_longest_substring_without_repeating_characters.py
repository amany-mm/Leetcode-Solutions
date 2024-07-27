"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Using sliding window technique
        Time complexity O(n)
        Space cimplexity O(n)
        """
        l = r = 0
        res = 0
        visited_set = set()

        # The left pointer moves to the right while marking visited characters
        # until the repeating character is no longer part of the current window.
        while r < len(s):
            while s[r] in visited_set:
                visited_set.remove(s[l])
                l += 1

            visited_set.add(s[r])
            # length of the current window (right - left + 1)
            res = max(res, r - l + 1)
            r += 1
        return res
