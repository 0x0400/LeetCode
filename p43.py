# https://leetcode.com/problems/multiply-strings/

from collections import defaultdict


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1List = [int(char) for char in reversed(num1)]
        num2List = [int(char) for char in reversed(num2)]
        tmp = defaultdict(int)
        for idx1, n1 in enumerate(num1List):
            for idx2, n2 in enumerate(num2List):
                num = n1 * n2
                remainder, mod = num % 10, num // 10
                tmp[idx1 + idx2] += remainder
                if mod:
                    tmp[idx1 + idx2 + 1] += mod

        for key in sorted(tmp.keys()):
            if tmp[key] >= 10:
                remainder, mod = tmp[key] % 10, tmp[key] // 10
                tmp[key] = remainder
                tmp[key + 1] += mod
        return "".join([str(tmp[key]) for key in reversed(sorted(tmp.keys()))])


if __name__ == "__main__":
    sol = Solution()
    # print(sol.multiply("2", "3"))
    print(sol.multiply("123", "456"))

