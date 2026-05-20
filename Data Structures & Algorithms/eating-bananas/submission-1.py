class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The upper bound for the answer will have to be at least len(piles) number of hours 
        # ceil (x / k) is the rate in which koko finishes the x pile 
        # upper bound for k is the largest pile in piles[] 
        # m is the largest pile and n is the number of piles 

        # upper_bound = max(piles)
        # lower_bound = 1 

        # piles_sorted = sorted(piles)

        # 4 / 2 = 2 
        # 25 / 10 = 18 not enough time 
        
        # the len of len(piles)

        r = max(piles)
        l = 1 
        res = r 

        while l <= r: 
            
            k = (l + r) // 2 
            totalTime = 0 

            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1 
            else:
                l = k + 1 
        return res