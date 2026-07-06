class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l, r = 0, 0
        max_freq = 0
        res = 0
        while r < len(s):
            count[ord(s[r]) - ord("A")] += 1
            print(s[l:r + 1], count,len(s[l:r + 1]), len(s[l:r + 1]) - max(count) <= k)
            if len(s[l:r + 1]) - max(count) <= k:
                res = max(res, len(s[l:r + 1]))
                r += 1
            else:
                count[ord(s[r]) - ord("A")] -= 1
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
        return res


