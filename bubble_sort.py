

def bubble_sort(arr):
    if(len(arr)==0):
        return arr
    swapped=False
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            # print("i,J",i,j)
            if arr[j]<arr[j-1]:
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
                swapped=True
        if not swapped:
            return arr#none of the elements are swapped means the array is already sorted so breaking the loop
    return arr



if __name__ == "__main__":
    arr=[7,3,8,2,6,1,4,6]
    print(bubble_sort(arr))
