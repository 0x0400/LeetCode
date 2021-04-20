# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 需要考虑 负数 的情况
        sign_part = ""
        if numerator * denominator < 0:
            sign_part = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

        int_part = 0
        if numerator > denominator:
            int_part = numerator // denominator
            numerator = numerator % denominator

        if numerator == 0:
            return sign_part + str(int_part)
        return "{}{}.{}".format(sign_part, int_part, self.getFraction(numerator, denominator))

    def getFraction(self, numerator: int, denominator: int) -> str:
        cache = {}
        nums = []
        i = 0
        while numerator != 0:
            numerator *= 10
            if numerator in cache:
                nums.insert(cache[numerator], "(")
                nums.append(")")
                return "".join(nums)

            if numerator < denominator:
                nums.append("0")
                cache[numerator] = i
                i += 1
                continue

            nums.append(str(numerator // denominator))
            cache[numerator] = i
            numerator = numerator % denominator
            i += 1
        return "".join(nums)
