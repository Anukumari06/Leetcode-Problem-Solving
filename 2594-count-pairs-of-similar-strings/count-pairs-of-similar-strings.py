class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d={}
        for w in words:
            ans=sorted(set(w))
            ans="".join(ans)
            if ans in d:
                d[ans]+=1
            else:
                d[ans]=1
        res=0
        for i in d:
            c=d[i]
            res+=(c*(c-1))//2
        return res
        
        
        


        
        



        

        