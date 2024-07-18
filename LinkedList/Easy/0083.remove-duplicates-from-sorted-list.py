""" 83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]
"""

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time complexity O(n)
        Space complexity O(1)

        Even there are 2 loops, time complexity is O(n)
        Because outer loop to traverse unique values and
        the inner loop to traverse duplicates.
        """
        current = head

        # outer loop for traverse linked list
        while current:

            # inner loop to check duplicates
            while current.next and current.val == current.next.val:
                current.next = current.next.next

            current = current.next

        return head
