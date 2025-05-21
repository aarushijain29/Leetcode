class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                op2, op1 = stack.pop(), stack.pop()
                if token == operators[0]:
                    stack.append(op1 + op2)
                elif token == operators[1]:
                    stack.append(op1 - op2)
                elif token == operators[2]:
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))
            else:
                stack.append(int(token))

        return stack[0]
