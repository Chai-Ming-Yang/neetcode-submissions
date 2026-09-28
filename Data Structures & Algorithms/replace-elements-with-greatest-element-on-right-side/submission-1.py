class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        count = Counter(arr)
        for i, x in enumerate(arr[:-1]):
            count[x] -= 1
            if count[x] == 0:
                del count[x]
            arr[i] = max(count)
        arr[-1] = -1
        return arr