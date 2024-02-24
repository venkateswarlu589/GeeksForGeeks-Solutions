#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        C = A
        D = B
        # code here 
        while A != B:
            if A > B:
                A = A - B
            else:
                B = B - A
        gcd = A
        lcm = int((C * D) // gcd)
        return [lcm,gcd]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends