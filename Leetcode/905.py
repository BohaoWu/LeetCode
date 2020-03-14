class Solution:
    def sortArrayByParity(self, List):
        odd = []
        even = []
        for i in List:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even.extend(odd)
        return even

def main():
    A = [3,1,2,4]
    solution = Solution()
    print(solution.sortArrayByParity(A))


if __name__ == '__main__':
    main()