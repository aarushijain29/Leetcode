class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, idx)
        max_area = 0

        for i in range(len(heights)):
            cur_height = heights[i]
            
            # This will track how far back this bar's rectangle can extend
            start = i

            # While the current bar is shorter than the last one in the stack,
            # it means the taller bar(s) can't extend beyond this point
            while stack and cur_height < stack[-1][0]:
                prev_h, prev_idx = stack.pop()
                max_area = max(max_area, prev_h * (i - prev_idx))
               
                # We update the start to the earlier index, because this shorter bar
                # can now potentially extend back as far as the popped one did
                start = prev_idx

            stack.append((cur_height, start))

        # Some bars may still be in the stack as these extended
        # all the way to the end of the histogram
        while stack:
            prev_h, prev_idx = stack.pop()
            max_area = max(max_area, prev_h * (len(heights) - prev_idx))
        
        return max_area
