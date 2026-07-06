class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l, r = 0, 1
        sub_set = set([s[l]])
        max_count = 1
        while r < len(s): # 1 < 4
            if s[r] in sub_set: # w in {'p','w'} >> False
                while s[r] in sub_set:
                    sub_set.remove(s[l]) # {'v'}
                    l += 1 # 1
            else:
                sub_set.add(s[r]) # {'p','w'}
                print(sub_set)
                max_count = max(max_count, r - l + 1) # 1 - 1 + 1
                r += 1 # 2
                
            
        return max_count