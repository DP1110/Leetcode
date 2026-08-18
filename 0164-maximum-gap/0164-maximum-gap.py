class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        lo = min(nums)
        hi = max(nums)
        if lo == hi:
            return 0

        bucket_size = max(1, (hi - lo) // (n - 1))
        bucket_count = (hi - lo) // bucket_size + 1

        bucket_min = [None] * bucket_count
        bucket_max = [None] * bucket_count

        for x in nums:
            idx = (x - lo) // bucket_size
            if bucket_min[idx] is None or x < bucket_min[idx]:
                bucket_min[idx] = x
            if bucket_max[idx] is None or x > bucket_max[idx]:
                bucket_max[idx] = x

        result = 0
        prev_max = lo

        for i in range(bucket_count):
            if bucket_min[i] is None:
                continue  # empty bucket, skip
            result = max(result, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return result