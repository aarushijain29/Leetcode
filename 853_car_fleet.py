class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stats = [(position[i], speed[i]) for i in range(len(position))]
        # sort cars by pos since a car can only become a fleet with cars ahead of it (due to no passing)
        car_stats.sort()
        stack = []

        for i in range(len(car_stats) - 1, -1, -1):
            pos, sp = car_stats[i]
            # time taken by car to reach target
            cur_time = (target - pos)/sp
            # cur car's time > time taken by cars ahead then cur car cannot become a fleet with them since cars ahead will reach target before cur car
            # so we add cur car's time to stack to check if cars behind cur car can become a fleet with cur car
            if not stack or cur_time > stack[-1]:
                stack.append(cur_time)

        # stores unique times taken by fleets to reach target
        return len(stack)
