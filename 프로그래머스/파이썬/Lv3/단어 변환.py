max_v = 999999999
def check(begin, target, words, cnt, temp):
    global max_v 
    if max_v < cnt:
        return
    
    if begin == target:
        max_v = min(max_v, cnt)
        return
    
    for word in words:
        if begin != word:
            w_cnt = 0
            for i in range(len(begin)):
                if begin[i] != word[i]:
                    w_cnt += 1

                if w_cnt > 1:
                    break

            if w_cnt == 1 and word not in temp:
                temp.append(word)
                check(word, target, words, cnt + 1, temp)
                temp.pop()

def solution(begin, target, words):
    global max_v
    answer = 0
    cnt = 0
    
    if target not in words:
        return 0
    
    check(begin, target, words, 0, [])
    return max_v