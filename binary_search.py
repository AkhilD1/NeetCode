# Binary Search
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
# Your solution must run in 
# O(logn) time.
# Example 1:
# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3
# Example 2:
# Input: nums = [-1,0,2,4,6,8], target = 3
# Output: -1

def binary_search(nums, target):
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid +1
        elif nums[mid] > target:
            r = mid -1
    return -1
print(binary_search(nums = [-1,0,2,4,6,8], target = 4))