def loss(p):
    s_ = 0

    for i in range(len(p)):     #sigma(avg - p)**2
        s_ += (avg - p[i])**2
    
    return s_

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
        elif i != (len(data) - 1) and (j == (len(data[i]) - 1) or data[i][j+1] == -1):  #다음 행이 있고 마지막 열이 아거나 다음 데이터가 -1이면
            result[i][j] = data[i+1][0] - (data[i][j] - 1)
            
if -1 in data[len(data)-1]:  #마지막 -1로
    result[len(data)-1][data[len(data)-1].index(-1)-1] = -1
else:
    result[(len(data)-1)][len(data[len(data)-1])-1] = -1

#페이지 숫자 출력
print(result)

#페이지 나누기
days = int(input('days : '))

sum_ = 0        #페이지 합 구하기
for i in range(len(data)):
    for j in range(len(data[0])):
        if result[i][j] != -1:
            sum_ += result[i][j]
avg = sum_ / days

pages = [0]
strs = ['']
d = 0

for i in range(len(data)):
    for j in range(len(data[0])):   #지금과 늘리기 후를 (평균*지금날짜)를 기준으로 비교하고 늘리거나 통과
        if result[i][j] == -1:
            break

        pages_ = pages[:]       #pages_ = pages 이렇게 하면 메모리 포인터 자체가 복사됨
        pages_[d] += result[i][j]

        if loss(pages_) < loss(pages):
            pages[d] += result[i][j]
            strs[d] += str(i+1) + '-' + str(j+1) +  ' '
        elif d < (days-1):
            pages.append(0)
            strs.append('')
            d += 1

            pages[d] += result[i][j]
            strs[d] += str(i+1) + '-' + str(j+1) +  ' '

print(pages)
print(strs)

#tmp
basic7 = [61, 51, 49, 53, 50, 53, 41]
sim7 = [61, 45, 51, 57, 50, 53, 41]
sim8 = [40, 41, 42, 44, 47, 50, 53, 41]


print(loss(1, sim7))
print(loss(0, basic7))
print(loss(0, sim8))