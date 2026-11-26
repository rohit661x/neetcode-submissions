class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        #init left pointer at index 0 of array
        right = len(nums) - 1 
        #init right pointer at last index of array

        while left <= right : #halving loop of search area
            mid = (left + right) // 2 #floor division 
            #defined mid as index

            if nums[mid] == target: #if value of mid is target
                return mid
            
            elif nums[mid] < target: #if value of mid < target
                left = mid + 1
                #update new left pointer = right half of old array

            else: #else... , if value > target
                right = mid - 1
                #update new right pointer = left half of old array
        return -1 #nothing was found



            

