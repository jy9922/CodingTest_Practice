# ��������
# ó������ ���� �����͸� �ϳ��� ��� ������ ��ġ�� ����
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # ������ ����
  for j in range(i,0,-1): # ������� �� �ݺ�
    if array[j] < array[j-1]: # ���� �����ͷ� ũ�� ��
      #������, ������ ����
      array[j], array[j-1] = array[j-1], array[j]
    else: #�����Ͱ� �� �����ͺ��� ũ�� break
      break

print(array)