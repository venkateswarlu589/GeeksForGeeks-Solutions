#User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < 1:
                low = mid + 1
            elif arr[mid] == 1:
                if mid == 0 or arr[mid] != arr[mid-1]:
                    return mid
                else:
                    high = mid - 1
        return -1
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstIndex(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends