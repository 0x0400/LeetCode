# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    sign = -1 if left * right < 0 else 1
                    stack.append( sign  * (abs(left) // abs(right)))
        return stack[-1]
