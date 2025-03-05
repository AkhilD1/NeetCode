

# Container With Most Water
# Solved 
# You are given an integer array heights where heights[i] represents the height of the 


# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4

def container_mostwater(height):
    l = 0
    r = len(height)-1
    res = 0
    while l<r:
        area = min(height[l], height[r] ) * (r-l)
        res = max(res, area)
        if height[l] <= height[r]:
            l +=1
        else:
            r -=1
    return res
print(container_mostwater(height = [2,2,2]))