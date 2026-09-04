class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        res=[]
        dirt=[(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(starts):
            visited=set(starts)
            queue=deque(starts)
            while queue:
                r,c=queue.popleft()
                for dr,dc in dirt:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            return visited
        pacific_st=[]
        for r in range(rows):
            pacific_st.append((r,0))
        for c in range(cols):
            pacific_st.append((0,c))
        
        atlantic_st=[]
        for c in range(cols):
            atlantic_st.append((rows-1,c))
        for r in range(rows):
            atlantic_st.append((r,cols-1))

        pacific=bfs(pacific_st)
        atlantic=bfs(atlantic_st)

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res