class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2
        sum1 = sum2 = 0
        q1 = q2 = 0
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                sum1 += int(num[i])
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                sum2 += int(num[i])

        diff = sum1 - sum2
        total_q = q1 + q2
        if total_q % 2 == 1:
            return True
        diff += (q1 - q2) * 9 // 2
        return diff != 0