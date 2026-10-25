from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)
        for s in strs:
            word_key = [0] * 26
            for c in s:
                word_key[ord(c) - ord("a")] += 1
            hash_map[tuple(word_key)].append(s)
        return list(hash_map.values())




