# https://leetcode.com/problems/3sum-closest/#/description

class Solution(object):

    def closestNum(self, nums, target):
        low, height = 0, len(nums) -1
        while low + 1 < height:
            mid = (low + height) / 2
            if nums[mid] == target:
                return target
            elif nums[mid] < target:
                low = mid
            else:
                height = mid
        return nums[low] if abs(nums[low] - target) < abs(nums[height] - target) else nums[height]

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = sum(nums[:3])
        nums_len = len(nums)
        for first_idx in range(0, nums_len-2):
            for second_idx in range(first_idx+1, nums_len-1):
                left = target - nums[first_idx] - nums[second_idx]
                if left + abs(target - closest) < nums[second_idx]:
                    break
                closest_left = self.closestNum(nums[second_idx+1:], left)
                if closest_left == left:
                    return target
                current = nums[first_idx] + nums[second_idx] + closest_left
                if abs(target - current) < abs(target - closest):
                    closest = current
        return closest


