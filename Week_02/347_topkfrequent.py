import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = collections.Counter(nums)
        # get the min heap
        heap = []
        for num, freq in count.items():
            n = len(heap)
            if n < k:
                heapq.heappush(heap, (freq, num))
            elif heap[0][0] < freq:
                # replace the smallest one
                heapq.heapreplace(heap, (freq, num))
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res

# test:
# nums = [1, 1, 1, 2, 2, 3]
# print(topKFrequent(nums, 2))


