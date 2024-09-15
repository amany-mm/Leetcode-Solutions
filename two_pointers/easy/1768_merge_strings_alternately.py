"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Using two pointers
        Time complexity O(n) -> O(s + t)
        Space complexity O(n) -> O(s + t)
        """
        merged_str = ""
        i, j = 0, 0
        len_word1 = len(word1)
        len_word2 = len(word2)

        while i < len_word1 or j < len_word2:

            if i < len_word1:
                merged_str += word1[i]
                i += 1
            if j < len_word2:
                merged_str += word2[j]
                j += 1

        # still there are characters left in word, append them all at the end
        while i < len_word1:
            merged_str += word1[i:]
        while j < len_word2:
            merged_str += word2[j:]

        return merged_str

        """
        Using one pointers
        Time complexity O(n) -> O(s + t)
        Space complexity O(n) -> O(s + t)
        """

        # merged_str = ""
        # max_len = len(word1) + len(word2)

        # for i in range(max_len):
        #     if i < len(word1):
        #         merged_str += word1[i]

        #     if i < len(word2):
        #         merged_str += word2[i]

        # return merged_str
