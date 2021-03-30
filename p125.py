# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        startIdx = 0
        endIdx = len(s) - 1

        while startIdx < endIdx:
            if not s[startIdx].isalnum():
                startIdx += 1
                continue
            if not s[endIdx].isalnum():
                endIdx -= 1
                continue

            if s[startIdx].lower() != s[endIdx].lower():
                return False

            startIdx += 1
            endIdx -= 1

        return True
