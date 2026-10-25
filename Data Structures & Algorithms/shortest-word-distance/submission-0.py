class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        distance = float('inf')
        for i in range(len(wordsDict)):
            for j in range(len(wordsDict)):
                if wordsDict[i] == word1 and wordsDict[j] == word2:
                    distance = min(distance, abs(j - i))
        return distance