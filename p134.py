# https://leetcode.com/problems/gas-station/

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for idx in range(0, len(gas)):
            if self.canCompleteCircuitFromIdx(idx, gas, cost):
                return idx
        return -1

    def canCompleteCircuitFromIdx(self, begin: int, gas: List[int], cost: List[int]) -> bool:
        curIdx = begin
        curGas = gas[curIdx]
        while curGas >= cost[curIdx]:
            curGas -= cost[curIdx]
            curIdx = (curIdx + 1) % len(gas)
            curGas += gas[curIdx]
            if curIdx == begin:
                return True
        return False
