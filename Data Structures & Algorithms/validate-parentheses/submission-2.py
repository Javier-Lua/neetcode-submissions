class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {"[" : "]", "{" : "}", "(" : ")"}
        for c in s:
            if stack:
                if stack[-1] in hash:
                    if hash[stack[-1]] == c:
                        stack.pop()
                    else:
                        stack.append(c)
            else:
                stack.append(c)
        return not stack
            