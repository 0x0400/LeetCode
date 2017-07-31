# https://leetcode.com/problems/generate-parentheses/description/


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parentheses = [["("] * n]

        while n > 0:
            result = []
            for item in parentheses:
                item_len = len(item)
                # stop 是 item_len - n，是为了保证插入位置右侧有足够的 ( 与 ) 匹配
                for idx in range(item_len, item_len - n, -1):
                    chars = list(item)
                    chars.insert(idx, ")")
                    result.append(chars)
                    if chars[idx - 1] == ")":
                        break
            n -= 1
            parentheses = result

        return ["".join(item) for item in result]
