class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hash_map_s1 = {i:0 for i in range(ord("a"), ord("z") + 1)}
        hash_map_s2 = {i:0 for i in range(ord("a"), ord("z") + 1)}

        for i in range(len(s1)):
            hash_map_s1[ord(s1[i])] += 1
            hash_map_s2[ord(s2[i])] += 1

        matches = 0
        for i in range(ord("a"), ord("z") + 1):
            matches += (1 if hash_map_s1[i] == hash_map_s2[i] else 0)
 
        for r in range(len(s1), len(s2)):
            
            if matches == 26: return True
            l = r - len(s1) + 1
            print(matches, s2[l], s2[r])
            hash_map_s2[ord(s2[l - 1])] -= 1
            hash_map_s2[ord(s2[r])] += 1
            if hash_map_s1[ord(s2[l - 1])] == hash_map_s2[ord(s2[l - 1])]:
                matches += 1
            elif hash_map_s1[ord(s2[l - 1])] == hash_map_s2[ord(s2[l - 1])] + 1:
                matches -= 1
            if matches == 26: return True
            if hash_map_s1[ord(s2[r])] == hash_map_s2[ord(s2[r])]:
                matches += 1
            elif hash_map_s1[ord(s2[r])] == hash_map_s2[ord(s2[r])] - 1:
                matches -= 1

        return matches == 26

        