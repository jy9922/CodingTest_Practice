n = int(input())
people = list(map(int, input().split()))
team = 0
team_person = []

# �������� ���� ���谡���� �������� ����
people = sorted(people)

for i in range(len(people)):
  # �� �׷쿡 ��� �� �� �� �ֱ�
  team_person.append(people[i])

  # ���� �ش� ���� ����� ���� ���������� ���ų� ���ٸ�
  if len(team_person) >= people[i]:
    # �� ����
    team += 1
    # �� �׷� �ʱ�ȭ
    team_person = []
  else: 
    continue

print(team)
  
