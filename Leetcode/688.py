class Solution:

    def knightProbability(self, N: int, K: int, r: int, c: int):
        dp = [[0 for i in range(N)] for j in range(N)]
        loc = [(-1,2), (-1,-2), (1,-2), (1,2), (2,1), (-2,1), (2,-1), (-2,-1)]
        dp[r][c] = 1
        for i in range(K):
            dp_new = [[0 for m in range(N)] for n in range(N)]
            for j in range(N):
                for k in range(N):
                    for l in loc:
                        x = j + l[0]
                        y = k + l[1]
                        if x < 0 or x >= N or y < 0 or y >= N:
                            continue
                        dp_new[j][k] += dp[x][y]/8
            dp = dp_new

        return sum(map(sum, dp))


def main():
    A = [3, 2, 0, 0]
    solution = Solution()
    print(solution.knightProbability(3, 2, 0, 0))


if __name__ == '__main__':
    main()

