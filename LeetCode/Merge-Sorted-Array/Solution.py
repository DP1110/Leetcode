1class Solution(object):
2    def merge(self, nums1, m, nums2, n):
3        i = m - 1      # last valid element in nums1
4        j = n - 1      # last element in nums2
5        k = m + n - 1  # last position in merged array
6        
7        # Fill nums1 from the back
8        while i >= 0 and j >= 0:
9            if nums1[i] > nums2[j]:
10                nums1[k] = nums1[i]
11                i -= 1
12            else:
13                nums1[k] = nums2[j]
14                j -= 1
15            k -= 1
16        
17        # If nums2 still has elements, copy them over
18        # (If nums1 has leftovers, they're already in place)
19        while j >= 0:
20            nums1[k] = nums2[j]
21            j -= 1
22            k -= 1