"""
Repeated String Match

Problem:
--------
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

Example:
--------
with A = "abcd" and B = "cdabcdab".

abcd cdab
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
-----
The length of A and B will be between 1 and 10000. 
"""
import math

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # This solution works, but it times out for large B values
        multiplier = 1
        max_multiplier = math.ceil(len(B) / len(A)) + 1

        if len(A) < len(B):
                multiplier = math.ceil(len(B) / len(A))
                A = A * multiplier

        while multiplier <= max_multiplier:
            last_element = len(A) - len(B)
            for j in range(0, last_element + 1):
                if A[j:j + len(B)] == B:
                    return multiplier
            multiplier += 1
            A = A * multiplier

        return -1
                
A = "abcd"
B = "cdabcdab"

sol = Solution()
print(sol.repeatedStringMatch(A, B))