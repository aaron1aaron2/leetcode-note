class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) >= 2:
            import heapq
            heap = [-i for i in stones]
            heapq.heapify(heap) # defual is min heap
            
            while len(heap) > 1:
                y = heapq.heappop(heap)
                x = heapq.heappop(heap)
                if y != x:
                    heapq.heappush(heap, y-x) # It is directly used as negative
            return 0 if len(heap) == 0 else -heap[0]
        else:
            return 0 if len(stones) == 0 else stones[0]
        
