import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : lambda a, b: int(a / b)
        }
        stack = []
        
        def opsFun(s, a, b):
            if s in ops:
                return ops[s](a, b)

        for t in tokens:
            if t in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                temp = opsFun(t, op1, op2)
                stack.append(temp)
            else: 
                stack.append(int(t))
        return int(stack[-1])