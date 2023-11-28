class Solution:
	def solve(self,nums,n):
        if not nums:
            return
        mid = (len(nums)-1)//2
        self.ans.append(nums[mid])
        self.solve(nums[:mid],(n//2))
        self.solve(nums[mid+1:],(n//2))
        
    def sortedArrayToBST(self, nums):
        # code here
        n = len(nums)
        self.ans = []
        self.solve(nums,n)
        return self.ans

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	nums = list(map(int, input().split()))
	obj = Solution()
	ans = obj.sortedArrayToBST(nums)
	for _ in ans:
		print(_, end = " ")
	print()

# } Driver Code Ends