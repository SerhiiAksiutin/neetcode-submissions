class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False
        stack = []
        hash_map = {
            "]":"[",
            ")":"(",
            "}":"{"
        }

        for c in s:
            if c in hash_map.keys() and len(stack) != 0 and stack[-1] == hash_map[c]:
                stack.pop()
            else:
                stack.append(c)
            print(stack)
        return stack == []

