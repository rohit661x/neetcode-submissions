class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #array List[int], array's name is nums
        #if any value appears more than once in the array do somthing
        #if any value does not fit that citera then do somthing
        
        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False
        
            
            
