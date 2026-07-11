class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # hash_map_s1 = {i:0 for i in range(ord("a"), ord("z") + 1)}
        # hash_map_s2 = {i:0 for i in range(ord("a"), ord("z") + 1)}

        # for i in range(len(s1)):
        #     hash_map_s1[ord(s1[i])] += 1
        #     hash_map_s2[ord(s2[i])] += 1

        # matches = 0
        # for i in range(ord("a"), ord("z") + 1):
        #     matches += (1 if hash_map_s1[i] == hash_map_s2[i] else 0)
 
        # for r in range(len(s1), len(s2)):
        #     if matches == 26: return True
            
        #     index = ord(s2[r - len(s1)])
        #     hash_map_s2[index] -= 1
        #     if hash_map_s1[index] == hash_map_s2[index]:
        #         matches += 1
        #     elif hash_map_s1[index] == hash_map_s2[index] + 1:
        #         matches -= 1

        #     index = ord(s2[r])    
        #     hash_map_s2[index] += 1
        #     if hash_map_s1[index] == hash_map_s2[index]:
        #         matches += 1
        #     elif hash_map_s1[index] == hash_map_s2[index] - 1:
        #         matches -= 1

        # return matches == 26
        match_list = [0] * 26

        for i in range(len(s1)):
            match_list[ord(s1[i]) - ord('a')] += 1
            match_list[ord(s2[i]) - ord('a')] -= 1

        matches = 0
        for i in match_list:
            matches += (1 if i == 0 else 0)

        print(matches)

        for r in range(len(s1), len(s2)):
            print(match_list)
            if matches == 26: return True
            index = ord(s2[r - len(s1)]) - ord('a')
            match_list[index] += 1
            if match_list[index] == 0:
                matches += 1
            elif match_list[index] - 1 == 0:
                matches -= 1

            index = ord(s2[r]) - ord('a')
            match_list[index] -= 1
            if match_list[index] == 0:
                matches += 1
            elif match_list[index] + 1 == 0:
                matches -= 1

        return matches == 26

