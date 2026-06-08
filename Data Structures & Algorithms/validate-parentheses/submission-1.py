class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append(s[0])

        for i in range(1, len(s)):
            c = s[i]
            match c:
                case "]":
                    if stack and stack[-1] == "[":
                        top = stack.pop()
                    else:
                        return False
                case "}":
                    if stack and stack[-1] == "{":
                        top = stack.pop()
                    else:
                        return False
                case ")":
                    if stack and stack[-1] == "(":
                        top = stack.pop()
                    else:
                        return False
                case _:
                    stack.append(c)
        
        if not stack:
            return True
        else:
            return False
        