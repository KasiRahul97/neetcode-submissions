class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited=set()
        graph=defaultdict(list)
        for o,m in edges:
            graph[o].append(m)
            graph[m].append(o)
        if len(edges)!=(n-1):
            return False
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        dfs(0)
        return len(visited)==n