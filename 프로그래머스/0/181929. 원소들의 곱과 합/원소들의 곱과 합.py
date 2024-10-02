def solution(num_list):
    answer = 0
    gop = 1
    hap1 = 0
    hap2 = 0
    for i in num_list :
        gop *= i
        hap1 += i
    hap2 = hap1**2
    
    if gop < hap2 :
        answer = 1
    else:
        answer = 0
    return answer