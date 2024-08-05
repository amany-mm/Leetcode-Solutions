"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/description/

You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character. You can perform
this operation at most k times.
Return the length of the longest substring containing the same letter you can
get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        using sliding window technique
        Space complexity O(n)
        Time complexity O(1) => O(26 character) constant
        """
        count = {}

        l = 0
        max_frequency = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_frequency = max(max_frequency, count[s[r]])

            # If window size - max_frequency shouldn't exceed allowed
            # replacements (k), then shrink window size by moving
            # left pointer and update it's character count
            if (r - l + 1) - max_frequency > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
