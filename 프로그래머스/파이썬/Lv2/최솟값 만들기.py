def solution(A,B):
    min_v = 0
    
    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        min_v += A[i] * B[i]
        
    return min_v