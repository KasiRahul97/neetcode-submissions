class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for course,pre in prerequisites:
            graph[course].append(pre)
        inprogress=set()
        done=set()
        def dfs(course):
            if course in inprogress:
                return False
            if course in done:
                return True
            inprogress.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            done.add(course)
            inprogress.remove(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True