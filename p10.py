# https://leetcode.com/problems/regular-expression-matching/#/description
# 参考 https://discuss.leetcode.com/topic/22948/my-dp-approach-in-python-with-comments-and-unittest 的实现

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # match_table[i][j] 表示 p[:i] 和 s[:j] 的匹配情况
        match_table = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]

        # s 和 p 都是空字符串的情况
        match_table[0][0] = True

        # s 是空字符串
        for i in range(2, len(p)+1):
            if p[i-1] == "*":
                match_table[i][0] = match_table[i-2][0]

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i-1] == "*":
                    if match_table[i-1][j] or match_table[i-2][j]:
                        match_table[i][j] = True
                        continue
                    # * 匹配一个字符
                    match_table[i][j] = match_table[i-1][j-1] and (p[i-2] == s[j-1] or p[i-2] == ".")

                    if not match_table[i][j]:
                        # * 可能需要匹配多个字符的情况
                        match_table[i][j] = match_table[i][j-1] and(p[i-2]==s[j-1] or p[i-2] == ".")
                else:
                    match_table[i][j] =  match_table[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == ".")
        return match_table[-1][-1]
