class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {")":"(", "]":"[", "}":"{"}
        for c in s:
            # check for closing type
            if stack and c in hash_map: 
                # check fot parentheses type
                if stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []
        