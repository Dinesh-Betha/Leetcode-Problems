class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s

        ans= ''
        dixt = {i+1:'' for i in range(numRows)}

        row = 0
        direction = 1

        for i in s:
            dixt[row+1]+=i
            if row == 0:
                direction = 1

            elif row==numRows-1:
                direction = -1
            row += direction
        
        for i in range(1,numRows+1):
            ans+=dixt[i]

            
        return ans