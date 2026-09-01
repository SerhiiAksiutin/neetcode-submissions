class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}

        for c in s:
            hash_map[c] = hash_map.get(c, 0) + 1
        # print(hash_map)

        for i, char in enumerate(s):
            if hash_map[char] == 1:
                return i
        return -1


        

        
            
