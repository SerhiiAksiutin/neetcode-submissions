class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = collections.defaultdict(list)
        for s in strs:
            seq = [0] * 26
            for c in s:
                seq[ord(c) - ord("a")] += 1
            hash_map[tuple(seq)].append(s)
        return hash_map.values()
                


