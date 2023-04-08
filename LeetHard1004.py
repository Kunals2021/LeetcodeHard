# Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are all the permutations of 
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater 
# permutation of its integer. More formally, if all the permutations of the array are 
# sorted in one container according to their lexicographical order, then the next permutation 
# of that array is the permutation that follows it in the sorted container. 
# If such arrangement is not possible, the array must be rearranged as the lowest 
# possible order (i.e., sorted in ascending order).
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical
# larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.
from typing import List, Optional, ListNode

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # If no decreasing element found, array is in descending order, so reverse it
        if i == -1:
            nums.reverse()
            return
        
        # Find the next element greater than the decreasing element from the end
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # Swap the two elements
        nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the subarray to the right of the decreasing element
        nums[i+1:] = nums[i+1:][::-1]





# Find the index i such that nums[i] < nums[i+1] and nums[i+1:] is in descending order.
# If i is not found, then the list is already in its maximum permutation. Sort the list and return.
# Find the smallest element in nums[i+1:] that is greater than nums[i]. Swap it with nums[i].
# Reverse the elements from index i+1 to the end of the list.
# For example, let's say we have the list [1, 3, 5, 4, 2]:
# Starting from the right, we find the index i=2 such that nums[i] < nums[i+1] and nums[i+1:] is in 
# descending order: [1, 3, 5, 4, 2] -> i=2.
# We find that the smallest element in nums[i+1:] that is greater than nums[i] is 4. We swap it 
# with nums[i]: [1, 3, 5, 4, 2] -> [1, 3, 4, 5, 2].
# We reverse the elements from index i+1 to the end of the list: [1, 3, 4, 5, 2] -> [1, 3, 4, 2, 5].
# Thus, the next lexicographically greater permutation of [1, 3, 5, 4, 2] is [1, 3, 4, 2, 5].
# The code starts by finding the first decreasing element in the array from the end. 
# This is done by iterating from the second last element to the beginning of the array, and stopping 
# at the first element that is smaller than the element to its right. If no such element is found, 
# then the array is in descending order, so we simply reverse the entire array to get the next permutation.
# If a decreasing element is found, we then need to find the next element greater than the 
# decreasing element from the end. This is done by iterating from the end of the array to the 
# decreasing element, and stopping at the first element that is greater than the decreasing element.
# Once we have found the next greater element, we swap it with the decreasing element, and then 
# reverse the subarray to the right of the decreasing element to get the next lexicographically 
# greater permutation.