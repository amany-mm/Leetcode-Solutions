""" 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution 1: Iterative solution
        using pointers
        Time complexity T(n) = O(n)
        Space complexity M = O(1)
        """
        prev, curr = None, head

        while curr:
            tmp = curr.next

            curr.next = head
            prev = curr
            curr = tmp

        return prev

        """
        Solution 2: Recursive solution
        Time complexity T(n) = O(n)
        Space complexity M = O(n)
        """
        # TODO
