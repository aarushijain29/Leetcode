class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Find intersection point inside the cycle
        slow = fast = 0

        while True:
            # Move slow by one step, fast by two steps
            slow = nums[slow]            
            fast = nums[nums[fast]]      

            # When slow == fast, a cycle is detected
            if slow == fast:
                break

        # Step 2: Find the entrance to the cycle (duplicate number)
        # Reset one pointer to start (index 0), keep the other at meeting point
        # Both now move one step at a time; they'll meet at the cycle entrance
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        # Both pointers now point to the duplicate number
        return slow
