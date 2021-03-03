# https://leetcode.com/problems/text-justification/

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rst = []
        curWords = []
        curWidth = 0
        for word in words:
            if len(word) + curWidth + len(curWords) <= maxWidth:
                curWidth += len(word)
                curWords.append(word)
                continue

            if len(curWords) == 1:
                rst.append(curWords[0] + " " * (maxWidth - curWidth))
            else:
                spaceWidth = (maxWidth - curWidth) // (len(curWords) - 1)
                extraSpaceWidth = (maxWidth - curWidth) - (len(curWords) - 1) * spaceWidth
                for i in range(0, extraSpaceWidth):
                    curWords[i] += " "
                # if extraSpaceWidth > 0:
                #     curWords[0] +=  " " * extraSpaceWidth
                spaces = " " * spaceWidth
                rst.append(spaces.join(curWords))
            curWords = [word]
            curWidth = len(word)

        tmp = " ".join(curWords)
        rst.append(tmp + " " * (maxWidth - len(tmp)))
        return rst
