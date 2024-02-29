#User function Template for python3

class Solution: 
    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            mid_min = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[mid_min]:
                    mid_min = j
            arr[mid_min],arr[i] = arr[i],arr[mid_min]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends