"""
Rotate Array

Problem:
--------
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Idea:
start at (len(num) - k) and swap k items back
"""

class Solution:
    def rotate_one_back(self, nums):
        last_num = num[len(nums) - 1]
        for i in range(len(nums) - 2, 0, -1):
            nums[i + 1] = nums[i]
        nums[0] = last_num
        return nums

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # [1, 2, 3, 4, 5], 2
        # [4, 5, 3, 1, 2]
        # 
        k = k % len(nums)
        k_start = len(nums) - k - 1
        k_arr = nums[k_start + 1:]
        for i in range(k_start, -1, -1):
            nums[i + k] = nums[i] # swap forward
        for i in range(len(k_arr)):
            nums[i] = k_arr[i]
        return nums

sol = Solution()
print(sol.rotate_back([1, 2, 3, 4, 5, 6, 7], 3))

