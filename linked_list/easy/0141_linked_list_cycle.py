"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/description/

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Solution 1: 
        Using hashset to store each visited element
        Time complexity O(n)
        Space complexity O(n)
        """
        # TODO

        """
        Soution 2: 
        Using fast and slow two pointers technique
        Time complexity O(n)
        Space complexity O(1)
        """
        slow, fast = head, head

        while fast and fast.next:  # if not reach the end (Null)
            slow = slow.next  # move by 1 step
            fast = fast.next.next  # move by 2 steps

            if slow == fast:  # if they meet at a node, then there is a cycle
                return True

        return False
