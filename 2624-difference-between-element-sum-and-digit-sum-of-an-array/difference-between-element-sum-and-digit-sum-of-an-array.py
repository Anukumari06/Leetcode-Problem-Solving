class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n1=sum(nums)
        l=[]
        for i in nums:
            while(i>=10):
                l.append(i%10)
                i=i//10
            l.append(i)
        # print(l)
        l1=sum(l)
        ans=abs(n1-l1)
        return ans

