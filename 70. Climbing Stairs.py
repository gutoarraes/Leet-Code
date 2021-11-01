# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        while n > =0:
            if n % 2 == 0:
                n -= 2
                count += 2
            elif n == 1:
                count += 1
                n -= 1
        return count