
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[]
    right=[]
    for element in arr[:-1]:
        if element<=pivot:
            left.append(element)
        else:
            right.append(element)
            
    return quicksort(left)+[pivot]+quicksort(right)
            

arr=[10,7,8,9,1,5]

sorted_arr=quicksort(arr)
print(sorted_arr)
