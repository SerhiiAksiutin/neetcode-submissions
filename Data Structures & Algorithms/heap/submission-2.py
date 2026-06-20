class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1:
            parent = i // 2
            if self.heap[i] < self.heap[parent]:
                temp = self.heap[i]
                self.heap[i] = self.heap[parent]
                self.heap[parent] = temp
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) - 1 == 0: 
            return -1
        
        res = self.heap[1]
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        
        i = 1
        while i * 2 < len(self.heap):
            if i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i * 2 + 1] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = temp
                i = i * 2 + 1
            elif self.heap[i * 2] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = temp
                i = i * 2
            else:
                break

        return res

    def top(self) -> int:
        if len(self.heap) - 1 == 0:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            return
        
        self.heap += nums
        i = (len(self.heap) - 1) // 2
        
        while i > 0:
            j = i
            while j * 2 < len(self.heap):
                if j * 2 + 1 < len(self.heap) and self.heap[j * 2 + 1] < self.heap[j * 2] and self.heap[j * 2 + 1] < self.heap[j]:
                    temp = self.heap[j]
                    self.heap[j] = self.heap[j * 2 + 1]
                    self.heap[j * 2 + 1] = temp
                    j = j * 2 + 1
                elif self.heap[j * 2] < self.heap[j]:
                    temp = self.heap[j]
                    self.heap[j] = self.heap[j * 2]
                    self.heap[j * 2] = temp
                    j = j * 2
                else: 
                    break
            i -= 1

