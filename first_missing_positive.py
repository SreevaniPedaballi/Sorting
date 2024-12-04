"""
input=[3,2,-1,4]
output=1

input=[1,2,0]
output=3

input=[3,4,-1,1]
output=2

https://leetcode.com/problems/first-missing-positive/description/
"""

# def first_positive_num(arr):
def firstMissingPositive(self, arr):
    arr_length=len(arr)
    if arr_length==0:
        return arr
    i=0
    while i<arr_length:
        correct_idx=arr[i]-1
        if arr[i]>0 and arr[i]<arr_length and arr[i]!=arr[correct_idx]:
            temp=arr[i]
            arr[i]=arr[correct_idx]
            arr[correct_idx]=temp
        else:
            i=i+1
    print(arr)

    for i in range(arr_length):
        if arr[i]!=i+1:
            return i+1
    return arr[i]+1

if __name__=="__main__":
    # arr=[3,2,-1,4,-2]
    # arr=[3,4,-1,1]
    # arr=[1,2,0]
    # arr=[2,1,3,5,4,-1,-2]
    arr=[1,2,0]
    print(firstMissingPositive(arr))      