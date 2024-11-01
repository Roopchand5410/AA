def partition(arr,l,r):
  pivot=arr[r]
  i=l-1
  for j in range(l,r):
    if arr[j]<pivot:
      i=i+1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[r]=arr[r],arr[i+1]
  return i+1

def quick_sort(arr,l,r):
  if l<r:
    pi=partition(arr,l,r)
    quick_sort(arr,l,pi-1)
    quick_sort(arr,pi+1,r)
arr=[162,525,35,14,5,64,154]
quick_sort(arr,0,len(arr)-1)
print(arr)

output=[5, 14, 35, 64, 154, 162, 525]
