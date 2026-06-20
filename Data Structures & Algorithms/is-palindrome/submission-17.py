class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alpha_num(c):
            if ord('a') <= ord(c.lower()) <= ord('z') or \
               ord('0') <= ord(c) <= ord('9'):
                return True
            else:
                return False

        l, r = 0, len(s) - 1

        while l < r:
            while not is_alpha_num(s[l]) and l < r:
                l += 1
            while not is_alpha_num(s[r]) and l < r:
                r -= 1
            print(s[l], s[r])
            if s[l].lower() == s[r].lower():
                l, r = l + 1, r - 1
                continue
            else:
                return False
        return True
            
            
    
    
        