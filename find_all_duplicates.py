"""
The array num have itegers from 1 to N
each element in array is repeate once or twice.
return an array of all integers that appears twice

eg:
input: num=[4,3,2,7,8,2,3,1]
output:[2,3]

input:[1,1,2]
output:[1]

solution: all the index at wrong index is the answer
"""

def find_duplicate_nums(arr):
    arr_length=len(arr)
    if(arr_length == 0):
        return arr
    i=0
    res_arr=[]
    while i< arr_length:
        correct_idx=arr[i]-1
        if correct_idx < arr_length and arr[i]!=arr[correct_idx]:
            temp=arr[i]
            arr[i]=arr[correct_idx]
            arr[correct_idx]=temp
        else:
            i=i+1
    print(arr)
    for i in range(arr_length):
        if(arr[i]!=i+1):
            res_arr.append(arr[i])
    return res_arr

if __name__=="__main__":
    arr=[4,3,2,7,8,2,3,1]
    print(find_duplicate_nums(arr))
   