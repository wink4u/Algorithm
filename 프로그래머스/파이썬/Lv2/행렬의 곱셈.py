def solution(arr1, arr2):
    answer = []
    
    for arr in arr1:
        temp = []
        
        for i in range(len(arr2[0])):
            result = 0
            
            for j, num in enumerate(arr):
                result += num * arr2[j][i]
            
            temp.append(result)
        
        answer.append(temp)
        
    return answer
