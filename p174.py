# https://leetcode.com/problems/dungeon-game/

from typing import Dict, List
from collections import namedtuple


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rowLen = len(dungeon)
        colLen = len(dungeon[0])

        Point = namedtuple('Point', ['row', 'col', 'curVal'])

        states = {
            Point(0, 0, dungeon[0][0]): dungeon[0][0],
        }
        while True:
            newStates = {}
            for point, minVal in states.items():
                if point.row+1 < rowLen:
                    newPoint = Point(point.row+1, point.col, point.curVal + dungeon[point.row+1][point.col])
                    newStates[newPoint] = min(newStates.get(newPoint, minVal)  , newPoint.curVal)

                if point.col+1 < colLen:
                    newPoint = Point(point.row, point.col+1, point.curVal + dungeon[point.row][point.col+1])
                    newStates[newPoint] = min(newStates.get(newPoint, minVal)  , newPoint.curVal)

            if not newStates:
                break
            states = newStates

        minVal = None
        for point, val in states.items():
            if minVal is None:
                minVal = max(1, -point.curVal+1, -val+1)
            else:
                minVal = min(minVal, max(1, -point.curVal+1, -val+1))
        return minVal

    def calculateMinimumHPV2(self, dungeon: List[List[int]]) -> int:
        ''' 从终点往前递推
        '''
        rowLen = len(dungeon)
        colLen = len(dungeon[0])

        Point = namedtuple('Point', ['row', 'col'])

        # plans 保持的是要进入 point 节点，至少需要的点数
        plans: Dict[Point, int] = {
            Point(rowLen-1, colLen-1): max(1, 1-dungeon[rowLen-1][colLen-1])
        }
        while True:
            newPlans: Dict[Point, int] = {}
            for prevPoint, prevVal in plans.items():
                if prevPoint.row > 0:
                    curPoint = Point(prevPoint.row-1, prevPoint.col)
                    curVal = max(prevVal - dungeon[curPoint.row][curPoint.col], 1)
                    newPlans[curPoint] = min(newPlans.get(curPoint, curVal), curVal)

                if prevPoint.col > 0:
                    curPoint = Point(prevPoint.row, prevPoint.col-1)
                    curVal = max(prevVal - dungeon[curPoint.row][curPoint.col], 1)
                    newPlans[curPoint] = min(newPlans.get(curPoint, curVal), curVal)

            if not newPlans:
                break
            plans = newPlans
        return plans.pop(Point(0, 0))
