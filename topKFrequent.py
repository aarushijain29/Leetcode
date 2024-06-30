class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get frequency of each num in nums
        numsCount = Counter(nums)

        # create a bucket to store (count : int, values : List[int])
        bucket = [[] for i in range(len(nums))]

        for key, item in numsCount.items():
            bucket[item-1].append(key)

        # Return k most frequent numbers
        res = []

        for i in range(len(bucket) - 1, -1, -1):
            l = len(bucket[i])
            if k > 0 and l > 0:
                res+=bucket[i]
                k -= l

        return res
