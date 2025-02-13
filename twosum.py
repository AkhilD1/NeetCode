# Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.
# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
# Example 2:
# Input: nums = [4,5,6], target = 10
# Output: [0,2]
# Example 3:
# Input: nums = [5,5], target = 10
# Output: [0,1]

def two_sum(nums, target):
    #BruteForce
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [0,0]
print(two_sum(nums = [4,5,6], target = 10))

def two_sum(nums, target):
    #O(N) solution
    complement = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in complement:
            return [complement[diff], idx]
        complement[num] = idx
print(two_sum(nums = [4,5,6], target = 10))