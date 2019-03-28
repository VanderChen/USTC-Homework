import numpy as np
import random
import time

def rand_partition(arr,low,high): 
    i =  ( low-1 )        # index of smaller element 
    pivot = arr[random.randint(low,high)]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def partition(arr,low,high): 
    i =   ( low-1 )       # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        # pi = partition(arr,low,high) 
        pi = rand_partition(arr,low,high)
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  

  # Function to do Quick sort 
def rand_quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
        # pi = rand_partition(arr,low,high)
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
# Driver code to test above 


def main():
    for i in range(10):
        arr = np.random.rand(10000 * i) * 1000
        start_time = 0
        end_time = 0

        start_time = time.time()
        quickSort(arr,0,len(arr) - 1)
        end_time = time.time()
        quickSort_time = end_time - start_time

        start_time = time.time()
        rand_quickSort(arr,0,len(arr) - 1)
        end_time = time.time() 
        rand_quickSort_time = end_time - start_time

        print("The normal time is :",quickSort_time," The random time is :",rand_quickSort_time," The Delta time is :",(quickSort_time - rand_quickSort_time))
    
    # print ("Sorted array is:") 
    # for i in range(len(arr) - 1): 
    #     print ("%d" %arr[i]), 
    # pass

if __name__ == "__main__":
    main()
    pass