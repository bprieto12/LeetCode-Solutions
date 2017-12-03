"""
Palandrome Number
-----------------

Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # y, z = 0, x + 1
        # while x != 0:
        # 	y += (y * 10) + x % 10
        # 	x = x // 10
        # print(z - 1, y)
        # return (z - 1) == y
        str_x = str(x)
        if x < 0:
            unsigned_str = str_x[1:]
            return unsigned_str == unsigned_str[::-1]
        else:
            return str_x == str_x[::-1]

sol = Solution()
print(sol.isPalindrome(2147447412))