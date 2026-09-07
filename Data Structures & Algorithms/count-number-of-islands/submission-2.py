class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        islands=0
        def bfs(r,c):
            queue=deque([(r,c)])
            visited.add((r,c))
            while queue:
                row,col=queue.popleft()
                dirtns=[(0,1),(0,-1),(1,0),(-1,0)]
                for dr,dc in dirtns:
                    nr=dr+row
                    nc=dc+col
                    while 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1' and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and (i,j) not in visited:
                    islands+=1
                    bfs(i,j)
        return islands