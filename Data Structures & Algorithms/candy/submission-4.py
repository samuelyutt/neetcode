class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies_lr = [0] * len(ratings)
        for r in range(1, len(ratings)):
            if (ratings[r] > ratings[r - 1]):
                candies_lr[r] = candies_lr[r - 1] + 1
            elif (ratings[r] <= ratings[r - 1]):
                candies_lr[r] = min(candies_lr[:r])
        
        candies_rl = [0] * len(ratings)
        for l in range(len(ratings) - 2, -1, -1):
            if (ratings[l] > ratings[l + 1]):
                candies_rl[l] = candies_rl[l + 1] + 1
            elif (ratings[l] <= ratings[l + 1]):
                candies_rl[l] = min(candies_rl[l + 1:])

        candies = [0] * len(ratings)
        for i in range(len(candies)):
            candies[i] = max(candies_lr[i], candies_rl[i])
        
        ret = sum(candies) + (1 - min(candies)) * len(candies)
        return ret