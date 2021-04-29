# https://leetcode.com/problems/count-primes/

class Solution:
    # def countPrimes(self, n: int) -> int:
    #     if n <= 2:
    #         return 0
    #     primes = []
    #     for i in range(3, n, 2):
    #         for p in primes:
    #             if i % p == 0:
    #                 break
    #         else:
    #             primes.append(i)
    #     primes.append(2)
    #     return len(primes)

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        nums = [1] * n
        nums[0] = nums[1] = 0
        cnt = 0
        curIdx = 2
        while curIdx < n:
            if nums[curIdx] == 0:
                curIdx += 1
                continue
            cnt += 1
            multi = curIdx * 2
            while multi < n:
                nums[multi] = 0
                multi += curIdx
            curIdx += 2 if cnt > 1 else 1
        return cnt
