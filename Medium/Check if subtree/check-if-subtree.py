#User function Template for python3




'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case


class Solution:
    def check(self,tree1,tree2):
        global ans 
        if (tree1 is None and tree2 is not None) or (tree1 is not None and tree2 is None):
            ans.append(0)
            
        if (tree1 is None or tree2 is None)  :
            return None
                
        if tree1.data != tree2.data:
            ans.append(0)
        
        self.check(tree1.left,tree2.left)
        self.check(tree1.right,tree2.right)
       

    def dfs(self,T,S):
        global ans
        if T is None:
            return 
        
        if T.data == S.data:

            initlen=len(ans)
            self.check(T,S)
            finlen=len(ans)
            if initlen == finlen:
                ans.append(1)
        


        self.dfs(T.left,S)
        self.dfs(T.right,S)
          

    def isSubTree(self, T, S):
        global ans
        ans=[]
        self.dfs(T,S)
        
        return True if sum(ans)>0 else False

#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
import sys
sys.setrecursionlimit(1000000)
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        rootT=buildTree(input())
        rootS=buildTree(input())
        if Solution().isSubTree(rootT, rootS) is True:
            print("1")
        else:
            print("0")
# } Driver Code Ends