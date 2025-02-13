# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true
# Example 2:
# Input: s = "jar", t = "jam"
# Output: false
# Constraints:
# s and t consist of lowercase English letters.
def anagram(s, t):
    if len(s) != len(t):
        return False
    char_s = {}
    for i in s:
        if i in char_s:
            char_s[i] += 1
        else:
            char_s[i] = 1
    char_t = {}
    for j in t:
        if j in char_t:
            char_t[j] += 1
        else:
            char_t[j] = 1
    return char_s == char_t
print(anagram(s = "jar", t = "jam"))