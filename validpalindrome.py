# Valid Palindrome
# Solved 
# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
# Example 2:
# Input: s = "tab a cat"
# Output: false

def valid_palindrome(s):
    new = "".join(c.lower() for c in s if c.isalnum())
    l = 0
    r = len(new) -1
    while l < r:
        if new[l] != new[r]:
            return False
        l +=1
        r -=1
    return True
print(valid_palindrome(s = "tab a cat"))