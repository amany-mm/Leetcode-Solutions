"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/description/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different
locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
"""
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        using 2 nested loops
        Time complexity : O(m * n) 
        Space complexity:  O(1)
        """
        # TODO
        """
        using Hashing
        Time complexity : O(n) 
        Space complexity:  O(n)
        """

        # TODO
        """ 
        using 2 pointers technique
        Time complexity : O(m + n) 
        Space complexity:  O(1)
        """
        l1, l2 = headA, headB

        while l1 != l2:  # Traverse through the lists until they reach Intersection node

            # When one pointer reaches the end of its list, it is reassigned to the head of the other list
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1
