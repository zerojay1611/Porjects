def loss(p):
    s_ = 0

    for i in range(len(p)):     #sigma(avg - p)**2
        s_ += (avg - p[i])**2
    
    return s_
def making_lists(d_, l):
    lists_ = l[:]
    lists_[d_] += 1
    lists_[len(lists_) - 1] -= 1

    return lists_
def simulation(l):
    lists_ = l[:]
    pages_ = [0] * days
    strs_ = [''] * days
    tmp = 0

    for i in range(len(lists_)):
        for j in range(lists_[i]):
            pages_[i] += flatten_result[tmp]
            strs_[i] += flatten_strs[tmp] + ' '
            tmp += 1

    return loss(pages_), pages_, strs_




#입력데이터
data = [[11, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1], 
[15, 18, 24, 26, 37, 44, 64, 65, 68, 71, 76], 
[79, 86, 94, -1, -1, -1, -1, -1, -1, -1, -1], 
[101, 106, 111, 115, 138, -1, -1, -1, -1, -1, -1], 
[147, 150, 155, 171, 172, 173, -1, -1, -1, -1, -1], 
[177, 181, 182, 183, 194, 218, -1, -1, -1, -1, -1], 
[229, 230, 240, 248, 254, 264, 266, 288, -1, -1, -1], 
[289, 293, 306, 310, 319, 321, 322, -1, -1, -1, -1]]
result = data

#페이지 숫자 계산하기
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == -1:
            break
        
        if j != (len(data[i]) - 1) and data[i][j+1] != -1:  #마지막 열이 아니고 그다음이 -1이 아니면
            result[i][j] = data[i][j+1] - (data[i][j] - 1)
        elif i != (len(data) - 1) and (j == (len(data[i]) - 1) or data[i][j+1] == -1):  #다음 행이 있고 마지막 열이 이거나 다음 데이터가 -1이면
            result[i][j] = data[i+1][0] - (data[i][j] - 1)
            
if -1 in data[len(data)-1]:  #마지막 -1로
    result[len(data)-1][data[len(data)-1].index(-1)-1] = -1
else:
    result[(len(data)-1)][len(data[len(data)-1])-1] = -1

#페이지 숫자 출력
print(result)


#평탄화, 페이지 합 구하기
length = 0
flatten_result = []
flatten_strs = []
sum_ = 0

for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] == -1:
            break
        
        length += 1
        flatten_result.append(result[i][j])
        flatten_strs.append(str(i+1) + '-' + str(j+1))
        sum_ += result[i][j]

#페이지 나누기
days = int(input('days : '))
avg = sum_ / days


#lists 초기화
lists = []
for i in range(days):
    if i != (days - 1):
        lists.append(1)
    else:
        lists.append(len(flatten_result) - days + 1)
loss_tmp, pages, strs = simulation(lists)
d = 0

#데이터 구하기
for count in range(len(flatten_result)):
    lists_tmp = making_lists(d, lists)
    loss_new, pages_new, strs_new = simulation(lists_tmp)
    if loss_tmp > loss_new:
        pages, strs = pages_new[:], strs_new[:]
        loss_tmp = loss_new
        lists = lists_tmp
    else:
        d += 1

print(pages)
print(strs)








'''
평탄화
자연수 분할
분할을 순열화(https://alwaysemmyhope.com/ko/python/684260-get-all-permutations-of-a-numpy-array-python-numpy.html)

전체 페이지 숫자 분할(1, 1, 1, 1, 1) + 마지막에 남은거전부다
'''
