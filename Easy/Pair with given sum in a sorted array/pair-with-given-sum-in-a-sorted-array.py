#User function Template for python3


class Solution:
    def Countpair (self, arr, n, sum) : 
        #Complete the function
        hashmap = {}
        count = 0
        for i in range(len(arr)):
            diff = sum - arr[i]
            if diff in hashmap:
                count += 1
            hashmap[arr[i]] = i
        if count == 0:
            return -1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Solution().Countpair(arr, n, K)
    print(res)



# } Driver Code Ends