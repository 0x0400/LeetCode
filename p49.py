# https://leetcode.com/problems/group-anagrams/

from typing import List, Tuple

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for  item in strs:
            key = self.getStrPoint(item)
            if key not in cache:
                cache[key] = []
            cache[key].append(item)
        return cache.values()

    def getStrPoint(self, chars: str) -> Tuple[int]:
        a = ord('a')
        rst = [0] * (ord('z') - a + 1)
        for char in chars:
            rst[ord(char) - a] += 1
        return tuple(rst)

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))
    print(sol.groupAnagrams(["tin","ram","zip","cry","pus","jon","zip","pyx"]))
