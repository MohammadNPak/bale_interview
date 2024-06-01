from collections import deque

def binary_search(arr:list,t):
    """a python function to get first occurance of x index that 
     x >= t 

    Args:
        arr (list): a sorted python list
        t (int): value in binary search

    Returns:
        i (int): index of first x that  x>=t
    """
    if arr[-1]<t:
        return len(arr)
    
    l = 0
    r = len(arr)-1
    while l<=r:
        step = (r-l)//2
        mid = l+step
        if arr[mid]<t:
            l = mid+1
        else:
            r = mid-1
    while arr[l]>=t and l>=0:
        l-=1
    return l+1



def count_positive(arr):
    """count number grater than or equal to zero in 
    sorted horizontaly and verticaly matix 

    Args:
        arr (list):

    Returns:
        s (int): count of non negative number in arr
        order is less than O(nlog(n))
    """
    for i,row in enumerate(arr):
        L = binary_search(row["data"][:row["L"]],0)
        if L< row["L"]:
            for j,rowj in enumerate(arr[i:]):
                rowj["L"]=L
    s=0
    l = len(arr[0]["data"])
    for i,row in enumerate(arr):
        s+=l-row["L"]
    return s


def main():
    n = int(input())
    a=[]
    for i in range(n):
        row = list(map(int,input().split()))
        a.append({"data":row,"L":len(row)})
    print(count_positive(a))

if __name__=="__main__":
    main()

