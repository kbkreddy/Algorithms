import operator
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operator_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        i =0 
        while i<len(tokens):

            if self.is_integer(tokens[i]):
                stack.append(int(tokens[i]))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(operator_map[tokens[i]](val2,val1)))
            i+=1

        return stack[-1]

    def is_integer(self, s:str):
        try:
            int(s)
            return True
        except ValueError:
            return False
        





        