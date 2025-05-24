class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()  # Stores elements in decreasing order — front always has the current max
        res = []
        l = 0  # Left boundary of the sliding window

        for r in range(len(nums)):
            # Maintain decreasing order in deque:
            # Remove all elements smaller than nums[r] from the back
            # because they can never be the max if nums[r] is in the window
            while q and nums[r] > q[-1]:
                q.pop()
            
            # Add current element to the deque
            q.append(nums[r])
            
            # Once the window size reaches k, start recording results
            if r - l + 1 == k:
                # The max for the current window is at the front of the deque
                res.append(q[0])

                # If the element at the front of the deque is exiting the window,
                # remove it from deque
                if q[0] == nums[l]:
                    q.popleft()

                # Move the window forward
                l += 1
                
        return res
