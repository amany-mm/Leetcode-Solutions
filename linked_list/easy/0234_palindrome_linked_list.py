"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/description/

Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """ First solution:
        Using extra memory array (copy linked list into array), then using 2 pointers technique  on array
        Time complexity:  O(n)
        Space complexity: O(n)
        """
        # nums = []
        # while head:
        #     nums.append(head.val)
        #     head = head.next
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False

        #     l += 1
        #     r += 1

        # return False
        """
        Two pointers (slow and faster pointers technique)
        Time complexity O(n)
        Space complexity O(1)
        """
        slow = head
        fast = head

        # find middle (slow)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next

            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
