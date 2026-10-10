# Valid Palindrome
# 10.10.26

def isPalindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def palindromeOwnCode(s):
    a = s.lower()
    b=""
    for i in a:
        if i.isalnum():
            b = b + i
        if b==b[::-1]:
            return True
        else:
            return False

isPalindrome("A man, a plan, a canal: Panama")

isPalindrome("race a car")
