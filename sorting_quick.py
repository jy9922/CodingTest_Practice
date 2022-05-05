array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:#���Ұ� 1���� ��� ����
    return
  pivot = start
  left = start + 1
  right = end
  while(left <= right):
    #�ǹ����� ū �����͸� ã�� ������ �ݺ�
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    #�ǹ����� ���� �����͸� ã�� ������ �ݺ�
    while(right > start and array[right] >= array[pivot]):
      right -= 1
    if left > right: #�����ȴٸ� ���� �����Ϳ� �ǹ� ��ü
      array[right], array[pivot] = array[pivot], array[right]
    else: #�������� �ʾҴٸ� ���� �����Ϳ� ū ������ ��ü
      array[left], array[right] = array[right], array[left]
  
  #���� ���� ���� �κа� ������ �κп��� ���� ���� ����
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)