class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1 = cand2 = None
        cnt1 = cnt2 = 0
        for x in nums:
            if cand1 is not None and x == cand1:
                cnt1 += 1
            elif cand2 is not None and x == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = x
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = x
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = cnt2 = 0
        for x in nums:
            if x == cand1:
                cnt1 += 1
            elif x == cand2:
                cnt2 += 1
        n = len(nums)
        res = []
        if cnt1 > n//3:
            res.append(cand1)
        if cnt2 > n//3:
            res.append(cand2)
        return res