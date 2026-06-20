class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if len(s) == 1:
        #     return True
        L, R = 0, len(s) - 1

    

        while R > L:
            if not self.is_alphanum(s[L]):
                L += 1
                continue
            if not self.is_alphanum(s[R]):
                R -= 1
                continue
            
            print(s[L].lower(), s[R].lower())
            if s[L].lower() == s[R].lower():
                L += 1
                R -= 1
            else:
                return False
        return True

    def is_alphanum(self, c: str) -> bool:
        return ord("a") <= ord(c.lower()) <= ord("z") or \
                ord("0") <= ord(c) <= ord("9")

        