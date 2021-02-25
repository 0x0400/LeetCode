# https://leetcode.com/problems/rotate-image/

# 按边处理；从外圈到内圈
# 选定4个顶点，其他点通过距离这些顶点的距离来计算翻转后的坐标

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        sideAction = [
            {
                "source": {"rowStep": 0, "colStep" : 1},
                "target": {"rowStep": 1, "colStep" : 0},
            },
            {
                "source": {"rowStep": 1, "colStep" : 0},
                "target": {"rowStep": 0, "colStep" : -1},
            },
            {
                "source": {"rowStep": 0, "colStep" : -1},
                "target": {"rowStep": -1, "colStep" : 0},
            },
            {
                "source": {"rowStep": -1, "colStep" : 0},
                "target": {"rowStep": 0, "colStep" : 1},
            },
        ]

        totalLen = len(matrix)
        roundIdx = 0
        while roundIdx <= totalLen//2:
            roundLen = totalLen - roundIdx * 2 - 1
            sourcePoin = (roundIdx, roundIdx)
            sourceValues = []
            for sideCnt in range(4):
                targetBackup = []
                curAction = sideAction[sideCnt]
                targetPoin = (sourcePoin[0] + roundLen * curAction['source']['rowStep'], sourcePoin[1] + roundLen * curAction['source']['colStep'])
                if targetPoin == sourcePoin:
                    return
                for idx in range(0, roundLen):
                    curSrcPoint = (sourcePoin[0] + idx * curAction['source']['rowStep'], sourcePoin[1] + idx * curAction['source']['colStep'])
                    curTargetPoint = (targetPoin[0] + idx * curAction['target']['rowStep'], targetPoin[1] + idx * curAction['target']['colStep'])
                    targetBackup.append(matrix[curTargetPoint[0]][curTargetPoint[1]])
                    if not sourceValues:
                        matrix[curTargetPoint[0]][curTargetPoint[1]] = matrix[curSrcPoint[0]][curSrcPoint[1]]
                    else:
                        matrix[curTargetPoint[0]][curTargetPoint[1]] = sourceValues[idx]
                sourcePoin = targetPoin
                sourceValues = targetBackup
            roundIdx += 1
