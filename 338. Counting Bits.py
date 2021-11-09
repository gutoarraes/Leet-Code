# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> list[int]:
        answer = []
        for i in range(n+1):
            string = str(bin(i)[2:])
            current_sum = 0
            for j in string:
                current_sum += int(j)
            answer.append(current_sum)
        return answer

