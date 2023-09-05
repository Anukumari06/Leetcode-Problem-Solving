class Solution:
    def numSquares(self, n: int) -> int:

        def solve(idx,tar,l,dp):
            if idx==0:
                if tar%l[idx]==0:
                    return tar//l[idx]
                else:
                    return int(1e9)

            if dp[idx][tar]!=-1: return dp[idx][tar]

            b = solve(idx-1,tar,l,dp)

            a = int(1e9)
            if l[idx] <= tar: a = 1 + solve(idx,tar-l[idx],l,dp)

            dp[idx][tar]=min(a,b)
            return min(a,b)


        l=[]
        i=1
        while(i*i<=n):
            l.append(i*i)
            i+=1

        dp=[[-1 for _ in range(n+10)] for i in range(len(l))]
        return solve(len(l)-1,n,l,dp)