# https://leetcode.com/problems/maximal-network-rank/

from typing import List
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cities = defaultdict(set)
        for (city1, city2) in roads:
            cities[city1].add(city2)
            cities[city2].add(city1)

        keys = list(cities.keys())
        maxRank = 0
        for idx, city1 in enumerate(keys):
            for idx2 in range(idx+1, len(keys)):
                city2 = keys[idx2]
                rank = len(cities[city1]) + len(cities[city2])
                if city2 in cities[city1]:
                    rank -= 1
                maxRank = max(maxRank, rank)
        return maxRank
