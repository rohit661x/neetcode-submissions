import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            pile = [
            -weight for weight in stones
        ]
            heapq.heapify(pile)

            while len(pile) > 1:
                y = -heapq.heappop(pile)
                x = -heapq.heappop(pile)

                if x!= y:
                    heapq.heappush(pile, -(y - x))
                
            if pile:
                return -pile[0]
            return 0
