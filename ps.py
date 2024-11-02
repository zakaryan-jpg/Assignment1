# PS

numbers = "4 -6 7 8 -9 100 12 13 56 17"
a = list(map(int, numbers.split()))

k = 3
for i in range(1, len(a)):
   key = a[i]
   j=i-1
   while j >= 0 and key < a[j]:
     a[j+1] = a[j]
     j -= 1
   a[j+1] = key

ps = a[0:k]
ps = " ".join(map(str, ps))
print(ps)
