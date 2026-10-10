class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.lower()
        b=""
        for i in a:
            if i.isalnum():
                b = b + i
        if b==b[::-1]:
            return True
        else:
            return False
