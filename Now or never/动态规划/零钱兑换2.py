from typing import List


# 暴力递归法
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.helper(coins, 0, amount)

    def helper(self, coins, index, money):
        res = 0
        num = 0
        if index == len(coins):
            return 1 if money == 0 else 0

        while coins[index] * num <= money:
            res += self.helper(coins, index + 1, money - coins[index] * num)
            num += 1
        return res


# 哈希表缓存优化
class Solution:
    def __init__(self):
        self.map = {}

    def change(self, amount: int, coins: List[int]) -> int:
        return self.helper(coins, 0, amount)

    def helper(self, coins, index, money):
        res = 0
        num = 0
        if index == len(coins):
            return 1 if money == 0 else 0
        else:
            while num * coins[index] <= money:
                key = str(index + 1) + '_' + str(money - num * coins[index])
                if key in self.map:
                    res += self.map[key]
                else:
                    res += self.helper(coins, index + 1, money - num * coins[index])
                    num += 1
        self.map[str(index) + '_' + str(money)] = res
        return res


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pass
