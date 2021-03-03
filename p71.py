# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        words = []
        curWord = ""
        for char in path:
            if char != "/":
                curWord += char
                continue

            if not curWord:
                continue

            if curWord == ".":
                pass
            elif curWord == "..":
                if words:
                    words.pop()
            else:
                words.append(curWord)
            curWord = ""
        if curWord:
            if curWord == ".":
                pass
            elif curWord == "..":
                if words:
                    words.pop()
            else:
                words.append(curWord)
        return "/" + "/".join(words)
