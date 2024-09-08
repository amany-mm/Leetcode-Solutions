"""
412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n+1):  # string array answer (1-indexed)
            if i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')

            elif i % 3 == 0:
                answer.append('Fizz')

            elif i % 5 == 0:
                answer.append('Buzz')

            else:
                answer.append(str(i))

        return answer
