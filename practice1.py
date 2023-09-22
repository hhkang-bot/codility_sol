# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    pass
    
    (bit_size, df) = divide(N)
    length_set = [0]
    l_tmp = 0
    length_set[l_tmp] = bit_size
    l_out = 0
   

    if df != 0:
        (bit_size, df) = divide(df)
        l_tmp = l_tmp + 1
        length_set = length_set + [bit_size]
        

        while df > 0:
            (bit_size, df) = divide(df)
            l_tmp = l_tmp + 1
            length_set = length_set + [bit_size]    
            
        length_out = [0 for l in range(l_tmp)]

        for t1 in range(l_tmp):
            tt = length_set[t1] - length_set[t1+1] - 1
            length_out[t1] = tt
            if t1 > 0:
                if length_out[t1] > l_out:
                    l_out = length_out[t1]
            else:
                l_out = length_out[t1]
    else:
        l_out = 0
    
    return l_out






def divide(N_tmp):
    i = 0
    while N_tmp >= 2**i:
        i = i + 1
    '''
    if N_tmp == 1:
        dif = 1
    else:
    '''
    dif = N_tmp - 2**(i-1)

    return i, dif