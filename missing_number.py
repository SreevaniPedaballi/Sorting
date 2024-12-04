"""
find missing num in 0 to N
"""
# Approach 1:
# def find_missing_num(arr):
#     if len(arr)==0:
#         return arr
    
#     sum = 0
#     for i in range(len(arr)+2):
#         sum=sum+i
#     arr_sum=0
#     for num in arr:
#         arr_sum=arr_sum+num
#     print("sum,arr_sum",sum,arr_sum)
#     return sum-arr_sum



# if __name__=="__main__":
#     arr=[3,2,1,5]
#     print(find_missing_num(arr))

# Approach 2:
"""
[0 4 3 1]
here the sequence is 0 1 2 3 4 and all the index positions also same.
if we didn't found index for example say 4 the index 4 not exists then ignore it
"""
def find_missing_num_using_cyclic_sort(arr):
    i=0
    while(i < len(arr)):
        correct_idx=arr[i]
        if(arr[i]< len(arr) and arr[i]!=arr[correct_idx]):
            temp=arr[correct_idx]
            arr[correct_idx]=arr[i]
            arr[i]=temp
        else:
            i=i+1
    print(arr)
    for idx in range(len(arr)):
        if(idx!=arr[idx]):
            return idx

if __name__=="__main__":
    arr=[4,2,1,3,6,0]
    print(find_missing_num_using_cyclic_sort(arr))