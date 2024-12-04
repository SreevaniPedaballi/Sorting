"""
Find All Numbers Disappeared in an Array
eg: 
1.input: [1,1]
output: [2]
length=2 so nums from 1 to 2

2.input: [4,3,2,7,8,2,3,1]
output:[5,6]
length: 8 so nums from 1 to 8

"""

# Approach 1:
# def find_missing_num(arr):
#     if len(arr)==0:
#         return arr
#     i= 0
#     sorted_arr=[0 for i in range(len(arr))]
#     while(i<len(arr)):
#         correct_idx=arr[i]-1
#         if correct_idx < len(arr) and sorted_arr[correct_idx]!=arr[i]:
#             sorted_arr[correct_idx]=arr[i]
#         i=i+1
#     print(sorted_arr)
#     res_arr=[]
#     for idx in range(len(sorted_arr)):
#         i=idx+1

#         if(sorted_arr[idx]!=i):
#             res_arr.append(i)
#     return res_arr


# Approach 2:
def find_missing_num(arr):
    if  len(arr) == 0:
        return arr
    i=0
    while(i<len(arr)):
        correct_idx=arr[i]-1
        if(correct_idx< len(arr) and arr[i]!=arr[correct_idx]):
            temp=arr[i]
            arr[i]=arr[correct_idx]
            arr[correct_idx]=temp
        else:
            i=i+1
    miss_nums=[]
    for i in range(len(arr)):
        correct_num=i+1
        if(arr[i]!=correct_num):
            miss_nums.append(correct_num)
    return miss_nums





if __name__=="__main__":
    # arr=[4,3,2,7,8,2,3,1]
    arr=[1,1]
    print(arr)
    print(find_missing_num(arr))
