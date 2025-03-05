# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
# Example 3:
# Input: strs = [""]
# Output: [[""]]
from collections import defaultdict
def group_anagram(strs):
    #Bruteforce sorting
    res = defaultdict(list)
    for s in strs:
        SortedS = "".join(sorted(s))
        res.append(SortedS)
    return list(res.values())
print(group_anagram(strs = ["act","pots","tops","cat","stop","hat"]))