# PAR3

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0] 
    left = []  
    right = [] 

    for x in arr[1:]: 
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)


numbers = "-68637 62698 41317 -86057 -69856 -35872 -90090 -55405 94767 -11032 86449"
a = list(map(int, numbers.split()))

par = quick_sort(a)
par = " ".join(map (str,par))
print(par)  
