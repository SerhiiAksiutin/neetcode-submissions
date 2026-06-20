class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s, set_t = {}, {}

        for i in range(len(s)):
            set_s[s[i]] = 1 + set_s.get(s[i], 0)
            set_t[t[i]] = 1 + set_t.get(t[i], 0)
        return set_s == set_t

