# 삽입정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 데이터 선택
  for j in range(i,0,-1): # 순서대로 비교 반복
    if array[j] < array[j-1]: # 앞의 데이터로 크기 비교
      #스와프, 데이터 삽입
      array[j], array[j-1] = array[j-1], array[j]
    else: #데이터가 전 데이터보다 크면 break
      break

print(array)