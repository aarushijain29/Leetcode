class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        for key, val in freq_map.items():
            bucket[val].append(key)

        ans = []
        for i in range(len(bucket) - 1, 0, -1):
            ans += bucket[i]
            if len(ans) == k:
                return ans
        
        # Overall: O(N) where N = len(nums)
    
    def topKFrequentUsingMaxHeap(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        # O(N) where N = len(nums)
        freq_map = Counter(nums) 
        # O(U) where U = number of unique elements in nums
        freq_list = [(-val, key) for key,val in freq_map.items()]
        # O(U)
        heapq.heapify(freq_list)

        ans = []
        # O(k) for the for loop
        for i in range(k):
            # O(log U) for heappop
            ans.append(heapq.heappop(freq_list)[1])
        # Overall for loop: O(k * log(U))

        # Overall: O(N) + O(k * log(U))
        return ans
