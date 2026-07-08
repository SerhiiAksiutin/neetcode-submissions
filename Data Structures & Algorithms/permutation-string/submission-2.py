class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash_map_s1 = {i:0 for i in range(97, 123)}
        hash_map_s2 = {i:0 for i in range(97, 123)}

        for i in s1:
            hash_map_s1[ord(i)] = 1 + hash_map_s1.get(ord(i), 0)
        print(hash_map_s1)
        l, r = 0, len(s1) - 1
        for i in s2[l:r]:
            hash_map_s2[ord(i)] = 1 + hash_map_s2.get(ord(i), 0)
        while r < len(s2):
            hash_map_s2[ord(s2[r])] += 1
            matches = hash_map_s1 == hash_map_s2
            if matches:
                return True
            print(hash_map_s2, ord(s2[l]))
            hash_map_s2[ord(s2[l])] -= 1
            l += 1
            r += 1
        
        return False

        