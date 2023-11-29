#User function Template for python3

def rotate( arr, n):
    j = 1
    k = 0
    for i in range(len(arr)-1):
        temp = arr[k]
        arr[k] = arr[j]
        arr[j] = temp
        j += 1
    return arr
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends