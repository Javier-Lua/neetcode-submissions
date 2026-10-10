class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+" : 1, "-" : 1, "*" : 1, "/" : 1}
        for s in tokens:
            if s in ops:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if s == "+":
                    stack.append(op1 + op2)
                elif s == "-":
                    stack.append(op1 - op2)
                elif s == "*":
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2)) # round down
            else:
                stack.append(s)
        return int(stack[0])