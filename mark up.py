def sum_no(N):
    if(N >= 0):
        sum = 0
        for a in range(N,N*2+1):
            sum += a
            return sum
    else:
        sum = 0
        for b in range(N*2+1,N):
            sum += b
            return sum                                                                                                  
N =int(input("Enter N:"))
print(sum_no(N))
    
