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

        if dividend < divisor:
            return 0

        if divisor == 1:
            times = dividend * positive
            if times > 2147483647 or times < -2147483648:
                return 2147483647

        multiple_list = [Multiple(1, divisor)]
        while multiple_list[-1].value < dividend:
            max = multiple_list[-1]
            mul = Multiple(max.times + max.times, max.value + max.value)
            multiple_list.append(mul)

        times = 0
        left = dividend
        for mul in reversed(multiple_list):
            while left >= mul.value:
                times += mul.times
                left -= mul.value
        return times * positive
