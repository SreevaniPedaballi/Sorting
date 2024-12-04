"""
Array num have integers from 1 to n and it includes one 1 repeted number.Find the repeted number without changing array
eg: 
input: num=[1,3,4,2,2]
output: 2

input= num=[3,1,3,4,2]
output:3

"""

def find_duplicate_num(arr):
    if len(arr) == 0:
        return arr
    i=0
    while i<len(arr):
        correct_idx=arr[i]-1
        if(arr[i]!=i+1):
            if(arr[i]!=arr[correct_idx]):
                temp= arr[i]
                arr[i]=arr[correct_idx]
                arr[correct_idx]=arr[i] 
            else:
                i=i+1
        else:
            print(arr[i])
            break
    
if __name__=="__main__":
    # arr=[3,1,3,4,2]
    arr=[1,2,1]
    find_duplicate_num(arr)