class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a + b
                stack.append(res)
            elif c == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a - b
                stack.append(res)
            elif c == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a * b
                stack.append(res)
            elif c == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                res = a / b
                stack.append(res)
            else:
                stack.append(c)
        
        return int(stack[-1])
        