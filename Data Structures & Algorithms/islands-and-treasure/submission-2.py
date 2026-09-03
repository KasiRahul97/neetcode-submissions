class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        queue=deque()
        dirt=[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0 and (i,j) not in visited:
                    visited.add((i,j))
                    queue.append((i,j))
        while queue:
            r,c=queue.popleft()
            for dr,dc in dirt:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]!=-1:
                    visited.add((nr,nc))
                    queue.append((nr,nc))
                    grid[nr][nc]=grid[r][c]+1
        
                    
