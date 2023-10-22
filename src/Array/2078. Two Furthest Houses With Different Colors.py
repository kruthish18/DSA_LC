class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        n=len(colors)
        max_diff = 0
        
        for i in range(n):
            for j in range(i,n):
                if colors[j]!=colors[i]:
                    diff = j-i
                    max_diff = max(max_diff , diff)
        
        return max_diff