class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        output = temp = 0
        
        for i in range(len(arr)):
            if i >= 2 and (arr[i-2] > arr[i-1] < arr[i] or arr[i-2] < arr[i-1] > arr[i]):
                temp += 1
            elif i >= 1 and arr[i-1] != arr[i]:
                temp = 2
            else:
                temp = 1
            output = max(output, temp)
        
        return output