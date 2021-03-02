# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b

        rst = ""
        plus = 0
        for idx in range(len(a)-1, -1, -1):
            tmp = int(a[idx]) + int(b[idx]) + plus
            plus = tmp // 2
            rst = str(tmp%2) + rst
        if plus:
            rst = "1" + rst
        return rst
