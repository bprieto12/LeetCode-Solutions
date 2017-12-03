"""
Remove Duplicates

Problem:
--------
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Example:
--------
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_len = 0
        previous_value = None

        for i in range(len(nums)):
            if previous_value != nums[i]:
                nums[unique_len] = nums[i]
                unique_len += 1
                previous_value = nums[i]
        
        return unique_len

test1 = [1, 1, 2]
test2 = [1, 2, 3, 4]
test3 = [1, 1, 1, 1]
test4 = [1, 2, 2, 3]
test5 = [1, 2, 2, 2]


sol = Solution()
print(sol.removeDuplicates(test1) == 2)
print(sol.removeDuplicates(test2) == 4)
print(sol.removeDuplicates(test3) == 1)
print(sol.removeDuplicates(test4) == 3)
print(sol.removeDuplicates(test5) == 2)

 
