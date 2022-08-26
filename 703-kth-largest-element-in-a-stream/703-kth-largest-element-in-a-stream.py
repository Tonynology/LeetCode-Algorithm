class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)    # O(n)
        
        while len(self.heap) > k:   #O(nlogn) since if k = 1 (heappop is logn)
            heapq.heappop(self.heap)   

    def add(self, val: int) -> int:     # O(Mlogn). M is the times to call add function.
        heapq.heappush(self.heap, val) # O(logn)
        
        if len(self.heap) > self.k:     #O(logn)
            heapq.heappop(self.heap)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)