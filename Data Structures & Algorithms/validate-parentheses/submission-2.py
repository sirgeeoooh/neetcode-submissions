class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "{" or bracket == "[" or bracket == "(":
                stack.append(bracket)
            elif bracket == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif bracket == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif bracket == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        else:
            return True


            
