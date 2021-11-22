class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        computed = [0] * (n + 1)
        computed[1] = 1
        for i in range(2, n + 1):
            computed[i] = computed[i - 1] + computed[i - 2]
        return computed[n]
