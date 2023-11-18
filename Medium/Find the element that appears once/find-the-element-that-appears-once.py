#User function Template for python3
class Solution:
    def search(self, A, N):
        # your code here
        hashmap = {}
        for i in range(len(A)):
            if A[i] not in hashmap:
                hashmap[A[i]] = 1
            else:
                hashmap[A[i]] += 1
        for key,val in hashmap.items():
            if val == 1:
                return key


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends