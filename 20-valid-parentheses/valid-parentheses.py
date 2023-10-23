class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in ["(","[","{"]:
                st.append(i)
            else:
                if not st:
                    return False
                curr=st.pop()
                if curr=="(":
                    if(i!=")"):
                        return False
                if curr=="[":
                    if(i!="]"):
                        return False
                if curr=="{":
                    if(i!="}"):
                        return False
        if st:
            return False
        else:
            return True
                    
        