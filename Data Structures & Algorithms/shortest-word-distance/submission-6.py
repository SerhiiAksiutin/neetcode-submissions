class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        distance = float('inf')
        w1, w2 = None, None
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1 = i
            if wordsDict[i] == word2:
                w2 = i
            if w1 is not None and w2 is not None:
                distance = min(distance, abs(w1 - w2))
        return distance