"""
5,3,2,8,1,6,7
3,5,2,8,1,6,7
2,3,5,8,1,6,7
1,2,3,5,8,6,7
1,2,3,5,6,8,7
1,2,3,5,6,7,8
"""
def insertion_sort(arr):
    if len(arr) == 0:
        return arr
    for i in range(len(arr)-1):
      for j in range(i+1,0,-1):
        print("i,J",i,j)
        if arr[j] < arr[j-1]:
            temp=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp
        else:
          break
    return arr

if __name__ == "__main__":
  arr=[5,3,2,8,1,6,7]
#   arr=[5,3,4,1,2]
  print(arr)
  print(insertion_sort(arr))
          