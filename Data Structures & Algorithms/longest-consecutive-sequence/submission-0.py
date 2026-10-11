class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sorting takes O(n log n), problem wants O(n) -> hash set
        #A hash map isn't inherently less efficient. But storing additional information doesnt provide  an algorithmic advantage.

        #1. Convert array into a hash set: O(1) avg membership checks
        #2. Iterate through the hash set
        #3. Determine whether a number is the start of a sequence.
            # x starts a sequence if x - 1 does not exist.

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num -1 not in num_set:
                #start of a sequence

                current = num
                length = 1

                while current + 1 in num_set:
                    current+= 1
                    length += 1
                longest = max(longest, length)
        return longest
    