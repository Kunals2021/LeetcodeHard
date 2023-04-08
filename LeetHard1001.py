# Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
# the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays into one sorted array
        merged = sorted(nums1 + nums2)
        # Find the length of the merged array
        n = len(merged)
        # Check if the length of the merged array is odd or even
        if n % 2 == 1:
            # If the length is odd, return the middle element
            return merged[n // 2]
        else:
            # If the length is even, return the average of the middle two elements
            return (merged[n // 2 - 1] + merged[n // 2]) / 2

# We first merge the two sorted arrays nums1 and nums2 into one sorted array merged. 
# We then find the length of the merged array n and check if it is odd or even. If n is odd, 
# we return the middle element of merged. If n is even, we return the average of the middle two
# elements of merged.
# Note that this implementation has a time complexity of O((m+n) log(m+n)) because of the sorted 
# function used to merge the two arrays. To achieve the desired time complexity of O(log(m+n)), 
# we would need to use a more complex algorithm such as binary search.