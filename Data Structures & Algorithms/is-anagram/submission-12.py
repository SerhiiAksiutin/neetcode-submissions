class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = [0] * 26

        for i in range(len(s)):
            res[ord(s[i]) - ord("a")] += 1
            res[ord(t[i]) - ord("a")] -= 1
        for n in res:
            if n == 0:
                continue
            else:
                return False
        return True
        # s_hash, t_hash = {}, {}
        # for i in range(len(s)):
        #     s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
        #     t_hash[t[i]] = 1 + t_hash.get(t[i], 0)

        # return s_hash == t_hash

        