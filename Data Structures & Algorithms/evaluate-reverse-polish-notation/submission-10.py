import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        
        ops = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : lambda a, b: int(a / b)
        }
        def opsFun(s, a, b):
            if s in ops:
                return ops[s](a, b)

            
            

        stack = []
        
        for t in tokens:
            if is_integer(t):
                temp =int(t)
                stack.append(temp)
            elif is_integer(t) == False:
                if t in ops:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    temp = opsFun(t, op1, op2)
                    stack.append(temp)
        return int(stack[-1])