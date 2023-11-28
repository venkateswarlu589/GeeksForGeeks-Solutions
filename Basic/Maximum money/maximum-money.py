#User function Template for python3

class Solution:
    def maximizeMoney(self, N , K):
        # code here 
        sum= 0
        for i in range(N+1):
            if i % 2 != 0:
                sum += K
        return sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = map(int,input().split())
        
        ob = Solution()
        print(ob.maximizeMoney(N,K))
# } Driver Code Ends