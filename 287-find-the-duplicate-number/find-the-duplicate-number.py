class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for key in d:
            if d[key] > 1:
                return key
        