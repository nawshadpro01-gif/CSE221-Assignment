a=input().split()
b=int(a[0])
c=int(a[1])
arr1=input().split()
arr2=[]
for i in arr1:
    arr2.append(int(i))
left=0
right=b - 1
flag = False

while left < right:
  current_sum = arr2[left] + arr2[right]
  if current_sum == c:
    print(left + 1, right + 1)
    flag = True
    break
  elif current_sum < c:
    left += 1
  else:
    right -= 1

if not flag:
  print(-1)