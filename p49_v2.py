# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for  item in strs:
            key = "".join(sorted(list(item)))
            if key not in cache:
                cache[key] = []
            cache[key].append(item)
        return cache.values()


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))
    print(sol.groupAnagrams(["tin","ram","zip","cry","pus","jon","zip","pyx"]))
