"""
Non-decreasing Array

Problem:
--------
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:
-------- 
Input: [4,2,3]
Output: True
Explanation: You could modify the first 
4
 to 
1
 to get a non-decreasing array.

My Idea:
--------
Find the first place where the list is decreasing.  Two numbers create a decreasing subset.  Try to
see if removing either of those numbers makes the list non-decreasing.  If either removal does, then
the task is possible.
"""
def isNonDecreasing(nums):
    for i in range(0, len(nums) -1):
        if nums[i] > nums[i + 1]:
            return False
    return True

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        decreasingIndex = None
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                decreasingIndex = i
                break
        
        if decreasingIndex != None:
            remove_first = nums[:decreasingIndex] + nums[decreasingIndex + 1:]
            remove_second = nums[:decreasingIndex + 1] + nums[decreasingIndex + 2:]
            return (isNonDecreasing(remove_first) or isNonDecreasing(remove_second))
        else:
            return True
    
    def checkPossibility_BetterSolution(self, nums):
        timesSeenDecr = 0

        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1] and timesSeenDecr == 0:
                timesSeenDecr += 1
                if i == 0 or ((i + 2 <= len(nums) - 1) and nums[i] <= nums[i + 2]):
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
            elif nums[i] > nums[i + 1] and timesSeenDecr > 0:
                return False
        return True

    

sol = Solution()
print(sol.checkPossibility_BetterSolution([-1, 4, 2, 3]))