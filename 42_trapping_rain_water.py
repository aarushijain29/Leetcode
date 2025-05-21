class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        l, r = 0, len(height) - 1

        # the highest wall seen so far from the left and right
        left_max, right_max = 0, 0

        while l < r:
            # Update the max height on the left and right so far
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                # Since left_max is smaller, right side will always have a taller wall
                # So water trapped at current left depends on left_max
                res += left_max - height[l]
                l += 1
            else:
                # Since right_max is smaller or equal, left side is guaranteed to be taller
                # So water trapped at current right depends on right_max
                res += right_max - height[r]
                r -= 1 

        return res
