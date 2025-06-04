class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree[i] = number of prereqs for course i
        indegree = [0 for _ in range(numCourses)]
        # adj_lst[i] = number of courses which have course i as prereq
        adj_lst = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            indegree[crs] += 1        
            adj_lst[pre].append(crs)
        
        # courses with zero indegree means those courses don't have prereqs
        # they are ready to be taken now
        zero_indegree = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero_indegree.append(i)
        
        finish = 0
        while zero_indegree:
            course = zero_indegree.popleft()
            finish += 1
            for pre in adj_lst[course]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    zero_indegree.append(pre)
        
        return finish == numCourses
