class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            coins[bill] += 1
            change = bill - 5
            for coin in [20, 10, 5]:
                while coins[coin] and change >= coin:
                    coins[coin] -= 1
                    change -= coin
            if change != 0:
                return False
        return True
