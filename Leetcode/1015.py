class Solution:
    def smallestRepunitDivByK(self, K: int):
        if K == 1:
            return 1
        seed = 1
        count = 1
        for i in range(K):
            seed = (seed * 10 + 1) % K
            count = count + 1
            if seed % K == 0:
                return count
        return -1
