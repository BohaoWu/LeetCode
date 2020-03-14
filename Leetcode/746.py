class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        # 回溯法
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])


def main():
    A = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solution = Solution()
    print(solution.minCostClimbingStairs(A))


if __name__ == '__main__':
    main()

