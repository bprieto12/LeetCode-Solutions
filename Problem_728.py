"""
Self Dividing Numbers

Problem:
--------
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
The boundaries of each input argument are 1 <= left <= right <= 10000.

Example:
--------
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_dividing_nums = []

        for num in range(left, right + 1):
            stored_value = num
            isSelfDividing = True
            while num != 0:
                digit = num % 10
                if digit == 0 or (stored_value % digit) != 0:
                    isSelfDividing = False
                num = num // 10
            if isSelfDividing:
                self_dividing_nums += [stored_value]
        return self_dividing_nums

sol = Solution()
print(sol.selfDividingNumbers(1, 22))
                