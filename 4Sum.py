class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()
                
        def kSum(start, k, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    cur.append(nums[i])
                    kSum(i + 1, k - 1, target - nums[i])
                    cur.pop()
                return
            l = start
            r = len(nums) - 1

            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append(cur + [nums[l], nums[r]])
                    l += 1
                    while l < r and l > 0 and nums[l] == nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        
        kSum(0, 4, target)
        return res
