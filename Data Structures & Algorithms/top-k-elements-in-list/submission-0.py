class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        sorted_keys = sorted(freq, key=freq.get, reverse=True)
        return sorted_keys[:k]