class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x=True
        y=True
        z=True
        for i in range(9):
            count=[0]*10
            for j in range(9):
                if board[i][j]==".":
                    continue
                else:
                    count[int(board[i][j])]+=1
            for val in count:
                if val>1:
                    x=False
            if x==False:
                break 
        for i in range(9):
            count=[0]*10
            for j in range(9):
                if board[j][i]==".":
                    continue
                else:
                    count[int(board[j][i])]+=1
            for val in count:
                if val>1:
                    y=False
            if y==False:
                break 
        for i in range(0,9,3):
            for j in range(0,9,3):
                count=[0]*10
                for row in range(3):
                    for col in range(3):
                        value=board[row+i][col+j]
                        if value==".":
                            continue
                        else:
                            count[int(value)]+=1
                for val in count:
                    if val>1:
                        z=False
            if z==False:
                break
        if(x==False or y==False or z==False):
            return False
        else:
            return True