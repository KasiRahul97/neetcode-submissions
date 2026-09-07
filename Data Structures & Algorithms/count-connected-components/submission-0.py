class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        visited=set()
        for l,m in edges:
            graph[l].append(m)
            graph[m].append(l)
        def bfs(node):
            q=deque([node])
            visited.add(node)
            while q:
                cur=q.popleft()
                for neighbour in graph[cur]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)
        no=0
        for vertex in range(n):
            if vertex not in visited:
                bfs(vertex)
                no+=1
        return no
