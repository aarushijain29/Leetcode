class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indegree[i] = number of prereqs for course i
        indegree = [0 for _ in range(numCourses)]
        # adj_lst[i] = courses which have course i as prereq
        adj_lst = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj_lst[pre].append(crs)

        zero_indegree = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero_indegree.append(i)
        
        res = []
        while zero_indegree:
            pre = zero_indegree.popleft()
            res.append(pre)
            for crs in adj_lst[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    zero_indegree.append(crs)
        
        return res if len(res) == numCourses else []
