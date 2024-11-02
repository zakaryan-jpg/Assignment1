# iprb 

k = 20
m = 30
n = 26

def prob(k,m,n):
    sum = k+m+n
    tot_pairs = (sum * (sum -1))/2

    probability = ( ((k*(k-1))/2 * 1) + ((k*m) * 1) +  ((k*n) * 1) + ((m*(m-1))/2 * 0.75)
                  + ((m*n) * 0.5) ) / tot_pairs

    probability = round (probability, 6)
    return probability


print(prob(k,m,n))
