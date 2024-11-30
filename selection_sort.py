

def selection_sort(arr):
  if len(arr)==0:
    return arr
  for i in range(len(arr)):
    last=len(arr)-i-1
    max_idx=find_max(arr,0,last)
    temp=arr[last]
    arr[last]=arr[max_idx]
    arr[max_idx]=temp
  return arr  
      
def find_max(arr,start,end):
  max=start
  for i in range(start,end):
    if(arr[max]<arr[i]):
        max=i
  return max
  
if __name__ == "__main__":
    arr=[2,5,4,7,8,3,6,1]
    print(selection_sort(arr))
