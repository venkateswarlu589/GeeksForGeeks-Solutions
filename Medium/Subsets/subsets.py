#User function Template for python3

class Solution:
    def subsets(self, A):
        #code here
        result = []
        cur = []
        def dfs(i):
            if i >= len(A):
                result.append(cur.copy())
                return
            cur.append(A[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        result.sort()
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends