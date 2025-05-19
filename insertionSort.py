class Solution:
    def insertionSort(self, arr):
        #code here
        n=len(arr)
        for i in range(0,n):
            while i>0 and arr[i-1]>arr[i]:
                arr[i-1],arr[i]=arr[i],arr[i-1]
                i-=1
        return arr
