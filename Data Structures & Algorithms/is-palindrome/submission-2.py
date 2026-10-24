"""class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        if (s[::-1].lower()==s.lower()):
            return True
        return False"""
"""class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = "".join(char for char in s if char.isalnum()).lower()
        
        left = 0
        right = len(cleanString) - 1

        while left <= right:
            if cleanString[left] != cleanString[right]:
                return False
            left += 1
            right -= 1
        return True