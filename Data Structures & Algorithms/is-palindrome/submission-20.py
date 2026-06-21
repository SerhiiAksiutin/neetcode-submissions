class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(c: str) -> bool:
            if ord("a") <= ord(c.lower()) <= ord("z") or \
               ord("0") <= ord(c.lower()) <= ord("9"):
                   return True
            else:
                return False

        l, r = 0, len(s) - 1
        while l < r:
            while not isAlphaNumeric(s[l]) and l < r:
                l += 1
            while not isAlphaNumeric(s[r]) and l < r:
                r -= 1
            # print(s[l].lower(), "=",s[r].lower())
            if s[l].lower() != s[r].lower():
                return False
            else:
                l, r = l + 1, r - 1
        return True



        