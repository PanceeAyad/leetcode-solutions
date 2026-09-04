class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        pre_max=[0]*n
        pre_max[0]=nums[0]

        for i in range(1,n):
            pre_max[i]=max(pre_max[i-1],nums[i])

        suff_min=[0]*n
        suff_min[n-1]=nums[n-1]

        for i in range(n-2,-1,-1):
           suff_min[i]=min(suff_min[i+1],nums[i])
        for i in range(n):
            instability = pre_max[i] - suff_min[i]

            if instability <= k:
                 return i

        return -1     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna