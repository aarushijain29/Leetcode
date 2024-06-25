class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # when we encounter same number again, we skip it
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                # need to reduce a number in s to get s to 0
                if s > 0:
                    r -= 1
                # need to increase a number in s to get s to 0
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
