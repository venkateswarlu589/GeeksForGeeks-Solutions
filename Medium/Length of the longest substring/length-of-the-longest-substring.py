#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        char = set()
        l = 0
        maxii = 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            maxii = max(maxii,r-l+1)
        return maxii
        
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends