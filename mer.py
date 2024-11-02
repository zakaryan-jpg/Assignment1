#MER

numbers = "10 20 30 40"
left = list(map(int, numbers.split()))

numbers = "10 12 34"
right = list(map(int, numbers.split()))

def merge(left, right): 
    result = []
    while len(left) > 0 and len(right) > 0: 
      if left [0] <= right [0]:
        result.append(left.pop(0)) 
      else:
        result.append(right.pop(0))
    while len(left) > 0: 
      result.append(left.pop(0))
    while len(right) > 0: 
      result.append(right.pop(0))
    return result


r = merge(left,right) 
r = " ".join(map(str, r))
print(r)
