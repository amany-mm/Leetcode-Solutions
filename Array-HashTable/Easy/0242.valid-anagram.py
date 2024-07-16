"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution 1:
        Time complexity O(s+t) => O(n)
        Space complexity O(s+t) => O(n)
        """
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t

        """
        # Solution2: more pythonic way, may be not work in interviews
        from collections import Counter

        return Counter(s) == Counter(t)

        #######################
        # Solution 3
        # Run time O(nlogn)
        # Memory O(1)
        # This solution doesn't have better performance if we run it,
        # So may be we need to implement sorted

        return sorted(s) == sorted(t)
        """
