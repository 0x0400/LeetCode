# https://leetcode.com/problems/restore-ip-addresses/

from typing import List

class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restoreSubIpAddresses(s, 4)

    def restoreSubIpAddresses(self, s: str, segments: int) -> List[str]:
        if segments <= 0:
            return []

        if len(s) > segments * 3:
            return []

        if not s:
            return []

        if s[0] == "0":
            curSegment = "0"
            if segments == 1:
                return ["0"] if s == "0" else []
            else:
                rst = []
                for plan in self.restoreSubIpAddresses(s[1:], segments-1):
                    rst.append(curSegment + "." + plan)
                return rst
        else:
            if segments == 1:
                return [s] if int(s) <= 255 else []
            rst = []
            curSegment = s[:1]
            for plan in self.restoreSubIpAddresses(s[1:], segments-1):
                rst.append(curSegment + "." + plan)
            if len(s) >= 2:
                curSegment = s[:2]
                for plan in self.restoreSubIpAddresses(s[2:], segments-1):
                    rst.append(curSegment + "." + plan)
            if len(s) >= 3:
                if int(s[:3]) <= 255:
                    curSegment = s[:3]
                    for plan in self.restoreSubIpAddresses(s[3:], segments-1):
                        rst.append(curSegment + "." + plan)

        return rst
