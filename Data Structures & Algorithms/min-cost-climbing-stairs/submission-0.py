class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #cost = [10, 15, 20], 0
        #        0    1   2   3  len = 4

        cost.append(0)

        #start from (n-3) i.e. (4-3) = pos 1, since we have to look at the next two values and pos 2 only has next one value
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1]) 
