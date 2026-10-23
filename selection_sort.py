def selection_sort(array):
    n= len(array)
    
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if array[j]<array[min]:
                min=j
        array[i],array[min]=array[min],array[i]
            
    return array
print('selection_sort',selection_sort([23,4,56,12,44,6]))
        
def bubble_sort(arr):
    n= len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if arr[j+1]<arr[j]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swapped=True
        if swapped==False:
            break
    return arr

        
print('bubble_sort',bubble_sort([23,4,56,12,44,6]))

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

print('insertion_sort',insertion_sort([23,4,56,12,44,6]))

def partition(arr,low,high):
    pivot = arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)

        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)


a=[23,4,56,12,44,6]
quick_sort(a,0,len(a)-1)
print('quick sort' ,a)

def merge(arr,low,mid,high):
    left=arr[low:mid+1]
    right =arr[mid+1:high+1]
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
def merge_sort(arr,low,high):
    if low<high:

        mid=(low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)


a=[23,4,22,44,2,665,7,90]
merge_sort(a, 0, len(a) - 1)
print('mergesort',a)

def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left< n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heap_sort(arr):
    n=len(arr)
    for i in range((n//2)-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

arr = [4, 10, 3, 5, 1]

heap_sort(arr)

print(arr)
