"""
844. Backspace String Compare
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
"""


class Solution:

    def process_string(self, string):
        stack = []

        for char in string:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()

        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Using Stack
        Time complexity O(n)-> O(s+t)
        Space complexity O(n)
        """
        return self.process_string(s) == self.process_string(t)
