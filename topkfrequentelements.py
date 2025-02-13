# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.
# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]
import heapq
def topkfreq(nums, k):
    freq = {}
    res = []
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    heap = []
    for key, val in freq.items():
        heapq.heappush(heap, (val, key))
        if len(heap) >k:
            heapq.heappop(heap)
    res = []
    while heap:
        res.append(heapq.heappop(heap)[1])
    return res
print(topkfreq(nums = [1,2,2,3,3,3], k = 2))