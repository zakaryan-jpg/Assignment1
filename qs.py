# QS

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


numbers = "2 4 1 6 9 2 4 10"
a = list(map(int, numbers.split()))

qs = quick_sort(a)
qs = " ".join(map (str,qs))
print(qs)  
