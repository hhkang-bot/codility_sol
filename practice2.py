# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    pass
    if A == [] or K == 0:
        output = A
    else:
        len_A = len(A)
        # if K = len_A: original A
        A_stack = A + A
        num_it = K%len_A
        output = [0 for j in range(len_A)]
        for k in range(len_A):
            output[k] = A_stack[len_A-num_it+k]


    return output