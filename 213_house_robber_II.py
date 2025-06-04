class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0: return 0
        if 1 <= n <= 2 : return max(nums[0], nums[-1])

        second_last_house = nums[0]
        last_house = max(nums[0], nums[1])

        for i in range(2, n - 1): # include house 1, exclude house n
            cur_house = max(last_house, nums[i] + second_last_house)
            second_last_house = last_house
            last_house = cur_house
        
        max_incl_first = last_house

        second_last_house = nums[1]
        last_house = max(nums[1], nums[2])

        for i in range(3, n): # exclude house 1, include house n
            cur_house = max(last_house, nums[i] + second_last_house)
            second_last_house = last_house
            last_house = cur_house
        
        max_excl_first = last_house

        return max(max_incl_first, max_excl_first)
