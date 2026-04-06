class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for item in tokens:
            if item not in '+-/*':
                val = int(item)
                stack.append(val)
            elif item in '+-/*':
                val1 = stack.pop()
                val2 = stack.pop()
                if item == '+':
                    temp = val1 +val2
                    stack.append(temp)
                elif item == '-':
                    temp = val2 - val1
                    stack.append(temp)
                elif item == '*':
                    temp = val1 * val2
                    stack.append(temp)
                elif item == '/':
                    temp = int(val2 / val1) 
                    stack.append(temp)
        return stack[-1]
            
              
                    
    