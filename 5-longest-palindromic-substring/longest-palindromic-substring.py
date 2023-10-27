class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l=[]
        for i in range(len(s)):
            s1=""
            for j in range(i,len(s)):
                s1+=s[j]
                if(s1==s1[::-1]):
                    l.append(s1)
        mx=0
        for i in l:
            mx=max(mx,len(i))
        for ch in l:
            if(len(ch)==mx):
                return ch



            

            
        