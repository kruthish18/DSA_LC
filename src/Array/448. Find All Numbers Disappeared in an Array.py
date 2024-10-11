class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        count={}

        for i in range(1, len(nums)+1):
            count[i]=0

        for num in nums:
            if num in count:
                count[num] += 1

        for i in range(1, len(nums)+1):
            if(count[i]==0):
                result.append(i)

        return result                    