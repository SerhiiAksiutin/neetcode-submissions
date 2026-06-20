class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            l = [0] * 26
            for c in s:
                l[ord(c) - ord("a")] += 1
            res[tuple(l)].append(s)
        return res.values()
        