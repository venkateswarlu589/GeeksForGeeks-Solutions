#User function Template for python3

def isSubset( a1, a2, n, m):
    hashmap = {}
    for i in range(len(a2)):
        if a2[i] not in hashmap:
            hashmap[a2[i]] = 1
        else:
            hashmap[a2[i]] += 1
    for i in a1:
        if i in hashmap:
            if hashmap[i] > 1:
                hashmap[i] -= 1
            else:
                del hashmap[i]
    if len(hashmap) == 0:
        return "Yes"
    return "No"
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends