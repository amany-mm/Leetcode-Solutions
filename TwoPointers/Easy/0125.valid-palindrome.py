"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters 
include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while left < right and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1

        return True

    def alphaNum(self, ch) -> bool:
        """
        Alphanumeric characters include letters and numbers.
        A->Z or a->z or 0->9
        """
        return (
            ord('A') <= ord(ch) <= ord('Z') or
            ord('a') <= ord(ch) <= ord('z') or
            ord('0') <= ord(ch) <= ord('9')
        )
