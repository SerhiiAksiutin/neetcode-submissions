class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            j = start
            while s[j] != "#":
                j += 1
            end = j + int(s[start:j]) + 1
            res.append(s[j + 1: end])
            start = end
        return res 
            

