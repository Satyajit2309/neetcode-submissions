class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            ones = 0
            for j in range(i):
                if (1 << j) & i:
                    ones +=1
            
            res.append(ones)
        
        return res