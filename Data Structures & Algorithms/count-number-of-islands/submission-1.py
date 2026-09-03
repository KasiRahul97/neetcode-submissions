class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        queue=deque([])
        islands=0
        def bfs(sr,sc):
            visited.add((sr,sc))
            queue.append((sr,sc))
            while queue:
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]!='0':
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and (i,j) not in visited:
                    islands+=1
                    bfs(i,j)
        return islands