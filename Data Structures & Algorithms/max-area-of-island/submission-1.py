class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        max_area=0
        def bfs(r,c):
            queue=deque([(r,c)])
            visited.add((r,c))
            area=1
            while queue:
                r,c=queue.popleft()
                dirtns=[(0,1),(0,-1),(1,0),(-1,0)]
                for dr,dc in dirtns:
                    nr=r+dr
                    nc=c+dc
                    while 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        area+=1
            return area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    max_area=max(max_area,bfs(i,j))
        return max_area