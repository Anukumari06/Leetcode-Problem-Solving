class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack=[]
        # for i in range(len(s)):
        #     if(s[i]==")"):
        #         stack.append(s[i])
        #     if(s[i]=="("):
        #         curr=stack.pop()
        # if len(stack)==0 or top=="(" or current=="(":
        #     stack.append()
        open=0
        close=0
        for i in range(0,len(s)):
            if(s[i]=="("):
                open+=1
            else:
                if(open==0):
                    close+=1
                else:
                    open-=1
        return open+close

        
        

