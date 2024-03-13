class Solution:
    def pivotInteger(self, n: int) -> int:
        l=0
        s=sum(range(1,n+1))
        for i in range(1,n+1):
            l+=i
            if(l*2==s+i):
                return i
        return -1
        
        