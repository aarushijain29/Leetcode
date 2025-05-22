class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_calculator(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile/speed)
            return time

        l, r = math.ceil(sum(piles)/h), max(piles)
        min_speed = r
        while l <= r:
            m = l + (r - l)//2
            time = time_calculator(m)

            # at speed m, time taken is less than or equal to h
            # we can try checking speeds lesser than m to find min speed
            if time <= h:
                min_speed = min(min_speed, m)
                r = m - 1
            # at speed m, time taken > h i.e. speed is too less
            # need to increase speed to get lesser time
            else:
                l = m + 1
        
        return min_speed
