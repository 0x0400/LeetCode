
# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        dividend = [1]
        for i in range(2, n):
            dividend.append(dividend[-1]*i)
        dividend.reverse()

        nums = [str(i) for i in range(1, n+1)]
        rst = ""
        for div in dividend:
            charIdx, k = k//div, k%div
            # k = 0 表示是第 charIdx-1 个数字的最后一个组合
            if k == 0:
                charIdx = charIdx-1
            rst += nums[charIdx]
            nums.pop(charIdx)
            if k == 0:
                nums.reverse()
                break
        rst += "".join(nums)
        return rst
