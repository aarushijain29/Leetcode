class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # need to find len of largest subarray with two distinct integers (fruits)
        # fruit_map = {fruit type : last idx in the last valid subarray that the fruit type was found at}
        # e.g. in array [0, 0, 1, 2] with l = 0 and r = 2, fruit_map[0] = 1 as 0 was last found at idx 1 in subarray from l to r
        l, fruit_map = 0, defaultdict(int)
        total = -1

        for r in range(len(fruits)):
            # keep adding fruits in the basket
            fruit_map[fruits[r]] = r
            # until we obtain more than 2 distinct fruits
            while len(fruit_map) > 2:
                # if fruit[l] is the start of the current subarray and the only tree of type fruit[l]
                if fruit_map[fruits[l]] == l:
                    # then remove the tree to reduce number of distinct fruits
                    del fruit_map[fruits[l]]       
                # increment l to shrink the subarray until we get two distinct fruits 
                l += 1
            
            total = max(total, r - l + 1)
        
        return total
            
