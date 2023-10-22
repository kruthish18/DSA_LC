class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n=len(names)
        names_map = {}
        res= []
        
        for i in range(n):
            names_map[heights[i]] = names[i]
            
        heights.sort(reverse=True)
        
        for i in range(n):
            res.append(names_map[heights[i]])
            
        return res 