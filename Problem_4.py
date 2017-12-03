"""
Median of Two Sorted Arrays

Problem: 
--------
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example:
--------
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
       	def median(arr):
       		if len(arr) == 1:
       			return arr[0]
       		elif len(arr) == 2:
       			return (arr[0] + arr[1]) / 2
       		else:
       			split = len(arr) // 2
       			median_arr = [median(arr[:split]), median(arr[split + 1:])]
       			return median(median_arr)
       	return median(nums1 + nums2)

nums1 = [1]
nums2 = [4]

sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))
        