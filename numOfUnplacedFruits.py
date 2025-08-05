class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        output = 0

        for fruit in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = 0
                    break
            else:
                output += 1
            
        return output
