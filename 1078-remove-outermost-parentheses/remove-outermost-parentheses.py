class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        open=0
        close=0
        start=0
        for i in range(0,len(s)):
            if(s[i]=="("):
                open+=1
            elif(s[i]==")"):
                close+=1
            if(open==close):

                ans=ans+s[start+1:i]
                start=i+1
                open=0
                close=0
        return ans
