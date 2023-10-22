class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        mini = nums[0]
        maxi = 0
        
        for num in nums[1:]:
            maxi = max(maxi, num-mini)
            mini = min(mini, num)
            
        if maxi>0:
            return maxi
        else:
            return -1