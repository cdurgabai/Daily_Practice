lass Solution:
    def search(self,arr,key):
        # Complete this function
        l=0
        h=len(arr)-1
        while l<=h:
            m=(l+h)//2
            if arr[m]==key:
                return m
            if arr[l]<=arr[m]:
                if arr[l]<=key<=arr[m]:
                    h=m-1
                else:
                    l=m+1
            elif arr[m]<=arr[h]:
                if arr[m]<=key<=arr[h]:
                    l=m+1
                else:
                    h=m-1
        return -1
