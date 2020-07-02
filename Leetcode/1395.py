class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sum = 0
        for i in range(len(rating)):
            leftbigger = 0
            rightbigger = 0
            leftsmaller = 0
            rightsmaller = 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    leftsmaller += 1
                if rating[j] > rating[i]:
                    leftbigger += 1
            for j in range(i+1, len(rating)):
                if rating[j] < rating[i]:
                    rightsmaller += 1
                if rating[j] > rating[i]:
                    rightbigger += 1
            sum += leftbigger * rightsmaller + leftsmaller * rightbigger
        return sum