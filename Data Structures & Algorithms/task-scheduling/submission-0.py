class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #creates a dict of keys, freq
                               # count = { 'X' : 2, 'Y' : 2}
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap)  
                cnt += 1  #we add one to reduce count since they are in -ve
                if cnt:
                    q.append([cnt, time + n]) #add cycles remaining i.e cnt and (time + n) time at which we can add it to heap again
            
            if q and q[0][1] == time:     #if time = (time + n) for an element, it is ready to be processed again
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
