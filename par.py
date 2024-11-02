# PAR

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


numbers = "-75278 -19452 5699 92578 48665 -26921 72149 3277 71278 70791"
a = list(map(int, numbers.split()))

sort = quick_sort(a)
sort = " ".join(map(str,sort))

print(sort)  
