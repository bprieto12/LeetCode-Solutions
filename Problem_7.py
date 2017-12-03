"""
Problem:
--------
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only 
hold integers within the 32-bit signed integer range. For the
 purpose of this problem, assume that your function returns 0 
 when the reversed integer overflows.


Example:
--------
Input: 123
Output:  321

Input: 120
Output: 21
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        total = 0
        maxPermissible = 2**31 - 1
        minPermissible = -2**31
        
        # Getting the sign
        isNegative = (x < 0)
        sign = 1
        if isNegative: sign = -1
        
        x = abs(x) # Python's floor divide acts weird with negative numbers

        while x != 0:
        	total = (total * 10) + (x % 10)
        	x = x // 10

        newNum = sign * total
        if newNum > maxPermissible or newNum < minPermissible:
        	return 0
        return newNum

#int1 = 120
int2 = -123
# int3 = 123
sol = Solution()
# one = sol.reverse(int1)
two = sol.reverse(int2)
# three = sol.reverse(int3)
print(two)