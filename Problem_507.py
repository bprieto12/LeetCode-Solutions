"""
PERFECT NUMBER

Problem:
--------
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
--------
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note:
-----
The input number n will not exceed 100,000,000. (1e8)
"""
import math

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or num == 1: return False
        summation = 0
        
        root_n = math.floor(math.sqrt(num))

        for i in range(1, root_n + 1):
            if num % i == 0:
                summation += i + (num // i)

        return summation - num == nu

num1 = 28
sol = Solution()
print(sol.checkPerfectNumber(num1))