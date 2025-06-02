class Solution:
    def climbStairs(self, n: int) -> int:
        two_steps_behind = one_step_behind = 1
        for i in range(2, n + 1):
            cur_step = two_steps_behind + one_step_behind 
            two_steps_behind = one_step_behind
            one_step_behind = cur_step
        return one_step_behind
