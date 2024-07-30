"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative solution: using Dummy Node
        The idea is to use a temporary dummy node as the start of the result list.
        The pointer Tail always points to the last node in the result list,
        so appending new nodes is easy.
        Time complexity O(n + m) where n and m are the size of list1 and list2
        Space complexity O(n)
        """
        dummy = ListNode()
        tail = dummy  # to avoid edge case of empty linkedlist

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            # update it regardeless list node is inserted
            tail = tail.next

        # if only one list node is not null, we will tail the
        # remaining portion and insert it to the end of tail

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

        """
        Recursive solution
        Time Complexity: O(m + n)
        Space Complexity: O(m + n)
        """
