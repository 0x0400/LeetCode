# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        idx: int = 1
        rst: str = "1"

        while idx < n:
            curChar = rst[0]
            curCnt = 1
            curRst = ""
            for char in rst[1:]:
                if char == curChar:
                    curCnt += 1
                else:
                    curRst = "{}{}{}".format(curRst, curCnt, curChar)
                    curChar = char
                    curCnt = 1

            rst = "{}{}{}".format(curRst, curCnt, curChar)
            idx += 1

        return rst


if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))
    print(sol.countAndSay(4))
