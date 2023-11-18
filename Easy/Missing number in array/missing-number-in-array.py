#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        count = 0
        total_sum = n * (n+1) // 2
        for i in array:
            count += i
        return total_sum - count


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends