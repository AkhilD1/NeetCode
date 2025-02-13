# Last Stone Weight
# You are given an array of integers stones where stones[i] represents the weight of the ith stone.
# We want to run a simulation on the stones as follows:
# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.
# Return the weight of the last remaining stone or return 0 if none remain.
# Example 1:
# Input: stones = [2,3,6,2,4]
# Output: 1
import heapq
def last_stone_weight(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        if second > first:
            heapq.heappush(heap, first - second)
    heap.append(0)
    return abs(heap[0])
print(last_stone_weight(stones = [2,3,6,2,4]))