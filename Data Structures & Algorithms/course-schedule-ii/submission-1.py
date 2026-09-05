class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for course,pre in prerequisites:
            graph[course].append(pre)
        inprogress=set()
        done=set()
        order=[]
        def dfs(course):
            if course in inprogress:
                return False
            if course in done:
                return True
            inprogress.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            inprogress.remove(course)
            done.add(course)
            order.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order