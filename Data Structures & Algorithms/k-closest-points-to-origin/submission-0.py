class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            dist = math.sqrt(math.pow((0 - x), 2) + math.pow((0 - y), 2))
            heapq.heappush(heap, (dist, (x,y)))
        
        for i in range(k):
            dist, point = heapq.heappop(heap)
            res.append(list(point))
        
        return res