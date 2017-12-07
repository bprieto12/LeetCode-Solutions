"""
DAILY TEMPERATURES

Problem:
---------
Given a list of daily temperatures, produce a list that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. If there 
is no future day for which this is possible, put 0 instead.

Example:
--------
Given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note:
-----
The length of temperatures will be in the range [1, 30000]. Each temperature will
be an integer in the range [30, 100].
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Brute Force

        next_greatest = []
        for i in range(len(temperatures) - 1):
            next = 1
            for j in range(i + 1, len(temperatures)):
                if (j == len(temperatures) - 1) and temperatures[i] >= temperatures[j]:
                    next_greatest += [0]
                elif temperatures[i] < temperatures[j]:
                    next_greatest += [next]
                    break
                next += 1


        next_greatest += [0]
        return next_greatest


sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

