# INS

numbers = "2 4 1 6 9 20 3 6"
a = list(map(int, numbers.split()))

sum = 0
for i in range(1, len(a)):
   key = a[i]
   j=i-1
   while j >= 0 and key < a[j]:
     a[j+1] = a[j]
     j -= 1
     sum +=1
   a[j+1] = key 


print(sum)
