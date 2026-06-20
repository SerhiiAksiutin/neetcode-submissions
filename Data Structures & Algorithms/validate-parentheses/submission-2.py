class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if stack and c in hash_map:
                if stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []
        