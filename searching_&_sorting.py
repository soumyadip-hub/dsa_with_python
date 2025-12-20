# searching & sorting 
# linear search
def linear_search(arr,target):
    size = len(arr)
    for index in range(0,size):
        if(arr[index]) == target:
            return index
    return -1
my_list = [10,23,45,76,17,34]
target = 17
result = linear_search(my_list,target)
print(result)
#---------------------------------------------
# binary search
def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = (start + end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end = mid - 1
        else:
            start = mid + 1
    return -1

sorted_list = [10,13,16,23,45,67,87]
target = 87
result = binary_search(sorted_list,target)
print(result)
# -------------------------------------------

# sorting algorithms
#_____________Bubble sort algo__________

def bubble_sort(arr):
    n=len(arr)
    for passes in range(0,n):
        for j in range(0,n-1-passes):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

unsorted_list = [123,54,67,87,34,45,22]
sorted_list =bubble_sort(unsorted_list)
print("sorted Elements: ",sorted_list)
# ---------------------------------------
#____________selection sort algo_______________
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if (arr[j]<arr[min_index]):
                min_index = j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
unsorted_list = [12,34,65,1,3435,7,88]
sorted_list = selection_sort(unsorted_list)
print("sorted Elements:",sorted_list)
# ------------------------------------------
# __________insertion sort algo_____________
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]          # current element
        j = i - 1             # previous index

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # shift right
            j -= 1

        arr[j + 1] = key      # insert at correct position

    return arr

unsorted_list = [12, 41, 32, 5, 78, 2]
sorted_list = insertion_sort(unsorted_list)
print("sorted elements:", sorted_list)
