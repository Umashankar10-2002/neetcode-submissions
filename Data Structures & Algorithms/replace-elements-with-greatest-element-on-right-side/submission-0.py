class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        nhn = 0
        while i >= 0 :
            if i == len(arr) - 1:
                hn = arr[i]
                arr[i] = -1
                i = i - 1
            elif arr[i] <= hn:
                arr[i] = hn
                i = i - 1
            else:   
                nhn = arr[i]
                arr[i] = hn
                if nhn > hn:
                    hn = nhn
                i = i - 1
        return arr

