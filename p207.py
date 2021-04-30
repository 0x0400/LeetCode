# https://leetcode.com/problems/course-schedule/

from typing import Dict, List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depends: Dict[int, List[int]] = {}
        reversedDepends: Dict[int, List[int]] = {}
        for requisite in prerequisites:
            if requisite[0] not in depends:
                depends[requisite[0]] = []
            depends[requisite[0]].append(requisite[1])

            if requisite[1] not in reversedDepends:
                reversedDepends[requisite[1]] = []
            reversedDepends[requisite[1]].append(requisite[0])

        courses = [False] * numCourses
        while True:
            isFinishOne = False
            for idx, finished in enumerate(courses):
                if finished:
                    continue

                if depends.get(idx, []):
                    continue
                courses[idx] = True
                for dependIdx in reversedDepends.get(idx, []):
                    depends[dependIdx].remove(idx)
                isFinishOne = True
            if not isFinishOne:
                break
        return not (False in courses)
