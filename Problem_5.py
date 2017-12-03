"""
Longest Palindromic Substring

Problem:
--------
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example:
--------
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

def isPalandrome(word):
    # Palandrome if the word is the same forward and backward
    return word == word[::-1]


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # this works, but it's slow
        palandromes = {}

        for i in range(len(s) - 1):
            for j in range(i, len(s) + 1):
                substring = s[i:j + 1]
                if isPalandrome(substring):
                    palandromes[len(substring)] = substring

        return palandromes[max(palandromes)]


s = Solution()
print(s.longestPalindrome_2("babad"))