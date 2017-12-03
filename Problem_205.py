"""
Isomorphic Strings

Problem:
--------
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example:
---------
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
-----
You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mappedChars = {}

        for i in range(len(s)):
            if s[i] not in mappedChars:
                if t[i] in mappedChars.values():
                    return False
                mappedChars[s[i]] = t[i]
            if t[i] != mappedChars[s[i]]:
                return False
        return True

s1, t1 = "egg", "add"
s2, t2 = "foo", "bar"
s3, t3 = "paper", "title"
s4, t4 = "ab", "aa"

sol = Solution()
print(sol.isIsomorphic(s1, t1))
print(sol.isIsomorphic(s2, t2))
print(sol.isIsomorphic(s3, t3))
print(sol.isIsomorphic(s4, t4))