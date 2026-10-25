class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_dist = len(wordsDict)
        w1 = w2 = -1
        for i, word in enumerate(wordsDict):
            if word == word1:
                w1 = i
            elif word == word2:
                w2 = i

            if w1 != -1 and w2 != -1:
                min_dist = min(min_dist, abs(w1 - w2))
                if min_dist == 1:
                    return 1
        return min_dist