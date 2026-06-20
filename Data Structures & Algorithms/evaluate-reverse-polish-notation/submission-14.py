class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            else:
                stack.append(int(token))
            print(stack)
        return stack[0]
        