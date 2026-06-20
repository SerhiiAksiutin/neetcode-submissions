class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alpha_num(s: str) -> str:
            new = ""
            for c in s:
                if ord("A") <= ord(c) <= ord("Z") or \
                   ord("a") <= ord(c) <= ord("z") or \
                   ord("0") <= ord(c) <= ord("9"):
                   new += c.lower()
            return new
        new_s = alpha_num(s)

        return new_s == new_s[::-1]