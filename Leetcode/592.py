class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] == '-':
            expression = '0/1' + expression
        expression = expression.replace('-', '+-')
        frac_nums = []
        for i in expression.split('+'):
            tmp = [int(i) for i in i.split('/')]
            frac_nums.append(tmp)

        ans = [0, 1]
        for num in frac_nums:
            # 交叉相乘
            ans[0] = ans[0] * num[1] + ans[1] * num[0]
            ans[1] = ans[1] * num[1]
            gcd = self.gcd(abs(max(ans[0], ans[1])), abs(min(ans[0], ans[1])))
            ans[0] /= gcd
            ans[1] /= gcd
        if ans[0] == 0:
            return '0/1'
        return str(int(ans[0])) + '/' + str(int(ans[1]))

    def gcd(self, x, y):
        if(y == 0):
            return 1
        if(x == y):
            return x
        while (x % y != 0):
            tmp = x - y
            x = y
            y = tmp
            if y > x:
                tmp = x
                x = y
                y = tmp
            y = abs(y)
            x = abs(x)
        return min(x,y)

def main():
    solution = Solution()
    print(solution.fractionAddition("-5/1+8/1+1/1"))


if __name__ == '__main__':
    main()