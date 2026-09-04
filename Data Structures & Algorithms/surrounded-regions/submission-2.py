class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        dirt=[(0,1),(0,-1),(1,0),(-1,0)]
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    if r==0 or r==rows-1 or c==0 or c==cols-1:
                        q.append((r,c))
        def capture():
            while q:
                r,c=q.popleft()
                if board[r][c]=="O":
                    board[r][c]="T"
                    for dr,dc in dirt:
                        nr=r+dr
                        nc=c+dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            q.append((nr,nc))

        capture()
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"


