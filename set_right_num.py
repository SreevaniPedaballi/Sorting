"""
array num is holding integers from 1 to N but one number is repeated once.Find out the correct number
eg:
input: num=[2 1 4 6 2 5]
out=[2,3]

input=num=[1,2,3,3]
output=[3,4]
"""

def set_right_num(arr):
    arr_length=len(arr)
    if arr_length==0:
        return arr
    i =0 
    while i <arr_length:
        correct_idx=arr[i]-1
        if arr[i]!=arr[correct_idx] and correct_idx < arr_length:
            temp=arr[i]
            arr[i]=arr[correct_idx]
            arr[correct_idx]=temp
        else:
            i=i+1
    print(arr)
    res_arr=[-1,-1]
    for i in range(arr_length):
        if arr[i]!=i+1:
            res_arr=[arr[i],i+1]

    return res_arr

if __name__ == "__main__":
    # arr=[2,1,4,6,5,2]
    arr=[7,5,3,2,1,3,6]
    print(set_right_num(arr))

