import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # for i in range(len(nums2)):
        #     nums1.append(nums2[i])
        # nums1.sort()
        # sum1 = 0
        # for i in range(len(nums1)):
        #     sum1+=nums1[i]
        # res = sum1 / len(nums1)
        # return res
        
        num=nums1+nums2
        ans=statistics.median(num)
        return ans


        