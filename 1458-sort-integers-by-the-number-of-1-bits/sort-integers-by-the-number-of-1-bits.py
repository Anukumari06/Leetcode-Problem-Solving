class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        s=""
        l=[]
        for i in arr:
            s=bin(i)[2:].count("1")
            l.append([s,i])
        l.sort()
        ans=[]
        for i in l:
            ans.append(i[1])
        return ans
