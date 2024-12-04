def cyclic_sort(arr):
    i=0
    while i< len(arr):
        correct_index=arr[i]-1
        if arr[i]!=arr[correct_index]:
            temp= arr[correct_index]
            arr[correct_index]=arr[i]
            arr[i]=temp
        else:
            i=i+1
    return arr

if __name__=="__main__":
    arr=[3,4,2,1,5]
    print(cyclic_sort(arr))