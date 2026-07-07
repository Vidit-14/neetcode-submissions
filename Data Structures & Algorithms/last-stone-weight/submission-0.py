class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        for i in range(n):
            stones[i] = -stones[i]  #for making max heap we negate the values
        
        heapq.heapify(stones)

        while len(stones) > 1:
            A = -heapq.heappop(stones)
            B = -heapq.heappop(stones)

            if A > B:
                A = A - B
                heapq.heappush(stones, -A)
            else:
                continue
        
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0