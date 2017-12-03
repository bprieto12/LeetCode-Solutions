"""
Problem:
--------
Given a string, find the length of the longest substring without repeating characters.

Examples:
---------
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

abbwoilbabbyw

Algorithm:
----------
Iterate through the string creating a running list of characters unique characters
if you arrive at a character in the running list that already exists in the running list
then 
    1) Store the current running list in a dictionary with the length of the list as the key and the list as the value
    2) find the first time the character shows up in the running list and remove that element and the elements before it
Continue until you reach the end of the array

Running time: O(N * logN)
"""
import time
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = time.time()
        listLength2List_dict = dict()
        running_list = []

        if len(s) == 0: return 0

        for i in range(len(s)):
            if s[i] not in running_list:
                running_list += [s[i]]
                copy_list = running_list.copy() # need to create a copy because the list is changing dynamically
                listLength2List_dict[len(copy_list)] = copy_list
            else:
                running_list += [s[i]] # add the new letter to the running list
                repeat_letter_index = running_list.index(s[i])# find the index of the repeated letter
                running_list = running_list[repeat_letter_index + 1:] # keeping all of the values after the first instance of the character
        print(time.time() - start)
        return max(listLength2List_dict)

    def betterSolution(self, s):
        """
        Way better solution that I found in the comment board.  Runs in O(n) time
        """
        startT = time.time()
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        print(time.time() - startT)
        return maxLength

string4 = "aab"
string1 = "bbbbbb"
string2 = "pwwkew"
string3 = "bbtablud"
string5 = "bpfbhmipx"
sol = Solution()
print(sol.lengthOfLongestSubstring(string5))
print(sol.betterSolution(string5))
