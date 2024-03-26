#User function Template for python3

class Solution:
    def chartostr(self, arr,N):
        # code here
        string = ""
        for i in arr:
            string += i
        return string


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        N= int(input())
        arr =input().split()
        ob = Solution()
        print(ob.chartostr(arr,N))
# } Driver Code Ends