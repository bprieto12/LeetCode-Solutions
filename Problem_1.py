"""
Problem
--------
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example
--------
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]

[2, 7, 11, 15, 0, 0
 9, 13, 17, 18, 22, 26
 20, 24, 
]
"""

class Solution:

	def twoSums(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		numsDict = dict(zip((nums), range(len(nums)))) # placing the items into a dictionary for fast querying
		print(numsDict)
		# we use len(nums) - 1 because if we've gotten to the last element, there aren't two items to sum
		for i in range(len(nums) - 1):
			remainder = target - nums[i]
			if remainder in numsDict and numsDict[remainder] != i:
				return i, numsDict[remainder]


nums = [0, 6, 6, 3]
target = 12
solution = Solution()
print(solution.twoSums(nums, target))

