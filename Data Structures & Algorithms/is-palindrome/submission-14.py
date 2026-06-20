class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0:
            return False

        def is_alpha_num(c):
            if ord("a") <= ord(c.lower()) <= ord("z") or \
            ord("0") <= ord(c) <= ord("9"):
                return True
            else:
                return False

        l, r = 0, len(s) - 1
        while l < r:
            if not is_alpha_num(s[l]):
                l += 1
                continue
            if not is_alpha_num(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                r, l = r - 1, l + 1
        return True
            
                
