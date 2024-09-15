"""
2367. Number of Arithmetic Triplets
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. 
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

Example 1:
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
"""
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        """
        Brute force 3 loops
        Time complexity O(n^3)
        Space complexity O(1)

        Hashmap
        Time complexity O(n)
        Space complexity O(n)
        """

        visited = {}
        counter = 0

        for i in range(len(nums)):  # {num: i}
            visited[nums[i]] = i

        # 1 num
        # 2 (num + diff)
        # 3 (num + 2 * diff)
        for num in nums:
            if (num + diff) in visited and (num + 2 * diff) in visited:
                counter += 1

        return counter
