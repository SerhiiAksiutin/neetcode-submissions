class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hash_map = {}
        char_map = [0] * 26

        for c in s:
            char_map[ord(c) - ord('a')] += 1
            # hash_map[c] = hash_map.get(c, 0) + 1
        # print(hash_map)

        for i, c in enumerate(s):
            # if hash_map[c] == 1:
            if char_map[ord(c) - ord('a')] == 1:
                return i
        return -1


        

        
            
