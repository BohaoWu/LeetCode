class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern = [i for i in pattern]
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        d = {}
        for i in range(len(pattern)):
            if d.__contains__(pattern[i]):
                if d[pattern[i]] != str[i]:
                    return False
            elif str[i] in d.values():
                return False
            else:
                d[pattern[i]] = str[i]
        return True


def main():
    pattern = "abba"
    str = "dog dog dog dog"
    solution = Solution()
    print(solution.wordPattern(pattern, str))


if __name__ == '__main__':
    main()