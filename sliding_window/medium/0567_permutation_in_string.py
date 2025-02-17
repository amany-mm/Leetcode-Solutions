"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        In this problem, we need to find a substring in s2
        that is permutation of s1.

        Permutation means re-arranging the letters of s1.
        In other words, we can say that we need to find an anagram of s1 in s2.
        A string s is anagram of p, if it satisfies the following conditions,
        1. s should contain all the characters in p.
        2. Frequency of each character should be same in two strings.

        Now, we need to find anagram of s1 in s2.
        This can be done by finding all the substrings of length same as s1
        and check that substring is anagram or not.
        If it is anagram, then return true.
        otherwise check next substring.

        Time complexity O(n)
        Space complexity O(1)
        """
        mapp = [0] * 26
        for c in s1:
            mapp[ord(c) - ord('a')] += 1

        i, j, count_chars = 0, 0, len(s1)

        while j < len(s2):
            if mapp[ord(s2[j]) - ord('a')] > 0:
                count_chars -= 1
            mapp[ord(s2[j]) - ord('a')] -= 1
            j += 1

            if count_chars == 0:
                return True

            if j - i == len(s1):
                if mapp[ord(s2[i]) - ord('a')] >= 0:
                    count_chars += 1
                mapp[ord(s2[i]) - ord('a')] += 1
                i += 1

        return False
