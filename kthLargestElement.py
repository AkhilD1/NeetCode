# Kth Largest Element in an Array
# Solved 
# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
# Follow-up: Can you solve it without sorting?
# Example 1:
# Input: nums = [2,3,1,5,4], k = 2
# Output: 4
# Example 2:
# Input: nums = [2,3,1,1,5,5,4], k = 3
# Output: 4
import heapq
def kthLargestElement(nums, k):
    heap = [-l for l in nums]
    heapq.heapify(heap)
    while k > 1:
        heapq.heappop(heap)
        k -= 1
    return -heap[0]
print(kthLargestElement(nums = [2,3,1,1,5,5,4], k = 3))