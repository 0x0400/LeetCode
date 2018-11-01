# https://leetcode.com/problems/divide-two-integers/

class Multiple:
    def __init__(self, times, value):
        self.times = times
        self.value = value

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        positive = 1
        if dividend < 0:
            positive = -positive
            dividend = -dividend
        if divisor < 0:
            positive = -positive
            divisor = -divisor

        if divisor == 1:
            times = dividend * positive
            if times > 2147483647 or times < -2147483648:
                return 2147483647

        multiple_list = [Multiple(1, divisor)]
        def rdivde(dividend, divisor):
            if dividend < divisor:
                return 0
            while multiple_list[-1].value < dividend:
                max = multiple_list[-1]
                mul = Multiple(max.times + max.times, max.value + max.value)
                multiple_list.append(mul)
            for mul in reversed(multiple_list):
                if mul.value <= dividend:
                    times = mul.times
                    left = dividend - mul.value
                    break
            return times + rdivde(left, divisor)
        return rdivde(dividend, divisor) * positive
