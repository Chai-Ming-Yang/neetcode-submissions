class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        N, M = len(nums1), len(nums2)
        combined = []
        while i<N and j<M:
            if nums1[i] < nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1
        while i < N:
            combined.append(nums1[i])
            i += 1
        while j < M:
            combined.append(nums2[j])
            j += 1
        
        
        if (M + N) % 2 == 1:
            return combined[(M+N) // 2]
        else:
            mid = (M+N)//2
            return (combined[mid] + combined[(mid-1)]) / float(2)