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
        st=[]
        c=0
        for i in s:
            if i=="(":
                st.append(i)
            else:
                if st and st[-1]:
                    st.pop()
                else:
                    c+=1
        return c+len(st)
                 

        
        

