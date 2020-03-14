class Solution:
    def maxScoreSightseeingPair(self, A):
        tmp = A[0] + 0
        res = tmp + A[1] - 1
        for i in range(1, len(A)):
            res = max(res, tmp + A[i] - i)
            tmp = max(tmp, A[i] + i)
        return res


def main():
    A = [8, 1, 5, 2, 6]
    solution = Solution()
    print(solution.maxScoreSightseeingPair(A))


if __name__ == '__main__':
    main()