class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        hottest = 0

        for cur_day in range(len(temperatures) - 1, -1, -1):
            cur_temp = temperatures[cur_day]

            # if cur_temp is the hottest day so far, there won't be
            # warmer days after it so res for that day = 0 
            if cur_temp >= hottest:
                hottest = cur_temp
                continue
            
            days = 1
            # since cur_temp isn't the hottest day so far, we need to check the closest warmer day
            while temperatures[cur_day + days] <= cur_temp:
                # using results from days after cur_day
                days += res[cur_day + days]
            res[cur_day] = days
        
        return res
