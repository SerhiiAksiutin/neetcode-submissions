class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l, r = 0, 1
        max_count = 1
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
            else:
                l += 1
            max_count = max(max_count, len(s[l:r]))
        return max_count




            
        

        