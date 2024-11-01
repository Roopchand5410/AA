def insertion_sort(arr):
  for i in range(1,len(arr)):
    temp=arr[i]
    while i-1>=0 and arr[i-1]>temp:
      arr[i]=arr[i-1]
      i=i-1
    arr[i]=temp
  print(arr)
arr=[162,525,35,14,5,64,14]
insertion_sort(arr)

#output:[5, 14, 14, 35, 64, 162, 525]
