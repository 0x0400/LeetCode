# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vers1 = version1.split(".")
        vers2 = version2.split(".")

        if len(vers1) < len(vers2):
            vers1 += ["0"] * (len(vers2) - len(vers1))
        elif len(vers1) > len(vers2):
            vers2 += ["0"] * (len(vers1) - len(vers2))

        for i in range(0, len(vers1)):
            num1 = int(vers1[i])
            num2 = int(vers2[i])
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0
