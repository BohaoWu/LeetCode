class Solution:
    def findCircleNum(self, M) -> int:
        N = len(M)
        self.M = M
        self.stu_tag = [[0 for i in range(N)] for i in range(N)]
        tag = 0
        for i in range(N):
            for j in range(N):
                print(self.M[i][j], self.stu_tag[i][j])
                if self.M[i][j] == 1 and self.stu_tag[i][j] == 0:
                    tag = tag + 1
                    self.paint(i, tag, N)
                    self.paint(j, tag, N)
        return tag


    def paint(self, i, tag, N):
        for row in range(N):
            print(self.M[i][row], self.stu_tag[i][row])
            if self.M[i][row] == 1 and self.stu_tag[i][row] == 0:
                self.stu_tag[i][row] = tag
                self.paint(row, tag, N)
        return


def main():
    solution = Solution()
    print(solution.findCircleNum([[1,1,0], [1,1,0], [0,0,1]]))


if __name__ == '__main__':
    main()