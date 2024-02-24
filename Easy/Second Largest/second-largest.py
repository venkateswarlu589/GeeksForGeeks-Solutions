#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
		largest = second = float('-inf')
		for i in arr:
		    largest = max(i,largest)
		for i in range(len(arr)):
		    if largest != arr[i]:
		        second = max(second,arr[i])
		if second == float('-inf'):
		    return -1
		return second


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends