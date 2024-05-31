def find(arr, value):
    low = 0
    high = len(arr)-1
    while low<=high:
          mid = (low+high)//2
          if arr[mid] == value:
             return mid
          elif arr[mid] < value:
               low = mid+1
          else:
               high = mid-1
    raise ValueError("value not in array")