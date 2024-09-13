class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        leastDiff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                curDiff = target - s
                if curDiff == 0:
                    return s
                if abs(curDiff) < abs(leastDiff):
                    leastDiff = curDiff
                if curDiff < 0:
                    r -= 1
                else:
                    l += 1
        
        return target - leastDiff
