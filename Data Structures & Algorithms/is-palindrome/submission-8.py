class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=""
        for ch in s:
            if ch.isalnum():
                ns=ns+ch.lower()
        if ns==ns[::-1]:
            return True
        return False