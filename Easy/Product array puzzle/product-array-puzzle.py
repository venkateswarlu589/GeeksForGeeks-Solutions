#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        zeroes = 0
        full_product = 1
        for idx, i in enumerate(nums):
            if i == 0:
                zeroes += 1
                if zeroes > 1:
                    return [0] * len(nums)
                position = idx
            else:
                full_product *= i
        if zeroes:
            result = [0] * len(nums)
            result[position] = full_product
        else:
            result = [full_product//i for i in nums]
                
        return result
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends