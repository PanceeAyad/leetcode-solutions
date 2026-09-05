class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # [LEETHUB AI REVIEW]
        # Your code has a critical bug in the initialization of prefix_max.
        # Line: prefix_max=nums[0]
        # This overwrites the list [0]*n with an integer. Then prefix_max[i-1] fails because you can't index an integer.
        # Fix: prefix_max[0] = nums[0]
        
        # Also, check the problem constraints for "Stable Index".
        # Usually, a stable index i requires:
        # 1. max(nums[0..i]) - min(nums[i..n-1]) <= k
        # 2. AND often there is a length constraint like (i + 1) >= k or similar.
        # If the problem only asks for the condition max-min <= k, your logic (after fixing the bug) is correct.
        # If there is a length constraint, add it to the if check.
        
        n = len(nums)
        if n == 0: return -1
        
        prefix_max=[0]*n
        prefix_max[0]=nums[0] # FIXED: Initialize first element
        for i in range(1,n):
            prefix_max[i]=max(prefix_max[i-1],nums[i])
        
        suffix_min = [0] * n
        suffix_min[-1] = nums[n-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        for i in range(n):
            score = prefix_max[i] - suffix_min[i]

            if score <= k:
                  return i

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna