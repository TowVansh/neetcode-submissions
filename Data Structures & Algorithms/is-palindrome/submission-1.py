"""class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        if (s[::-1].lower()==s.lower()):
            return True
        return False"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]