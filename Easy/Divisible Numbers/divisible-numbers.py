#User function Template for python3

class Solution:
    def find(self,A,B): 
        # code her
        x = A + 1
        while True:
            if x % B == 0:
                return x
                break
            x += 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B = input().split()
        A = int(A)
        B = int(B)
        ob = Solution()
        print(ob.find(A,B))
# } Driver Code Ends