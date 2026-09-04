class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        queue=deque()
        dirt=[(0,1),(0,-1),(1,0),(-1,0)]
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        mins=0
        while queue:
            ls=len(queue)
            rotthismin=False
            for _ in range(ls):
                r,c=queue.popleft()
                for dr,dc in dirt:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]!=0 and grid[nr][nc]!=2:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        fresh-=1
                        rotthismin=True
            if rotthismin:
                mins+=1
            
        return mins if fresh==0 else -1
