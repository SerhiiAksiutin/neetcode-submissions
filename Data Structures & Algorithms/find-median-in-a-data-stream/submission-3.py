import heapq

class MedianFinder:

    def __init__(self):
        # two arrays: one small (max_heap) and one large (min_heap)
        self.max_heap, self.min_heap = [],[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -1 * num)
        
        # small and large can't differ more than by 1. It it is we should balance
        if len(self.max_heap) < len(self.min_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * val)

        if len(self.max_heap) + 1 > len(self.min_heap):
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # maximum in small can't be bigger tham minimum in large
        if self.max_heap and self.min_heap and (-1 * self.max_heap[0] > self.min_heap[0]):
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, val)

    def findMedian(self) -> float:
        # print(self.max_heap, self.min_heap)
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else:
            return (-1 * self.max_heap[0] + self.min_heap[0]) / 2
        
        