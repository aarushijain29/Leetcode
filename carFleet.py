class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_coord = [(p, s) for p, s in zip(position, speed)]
        car_coord.sort()
        stack = [(target - car_coord[-1][0])/car_coord[-1][1]]

        for i in range(len(position) - 2, -1, -1):
            d = (target - car_coord[i][0])/car_coord[i][1]
            if stack[-1] < d:
                stack.append(d)

        return len(stack)
