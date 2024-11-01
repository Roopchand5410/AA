def bubble_sort(arr):
  for i in range(0,len(arr)):
    for j in range(0,len(arr)-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr
arr=[162,525,35,14,5,64,14]
bubble_sort(arr)
print(arr)

#ouput:[5, 14, 14, 35, 64, 162, 525]
