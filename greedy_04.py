n = int(input())
people = list(map(int, input().split()))
team = 0
team_person = []

# 공포도가 낮은 모험가부터 오름차순 정렬
people = sorted(people)

for i in range(len(people)):
  # 팀 그룹에 사람 한 명 씩 넣기
  team_person.append(people[i])

  # 만약 해당 팀의 사람의 수가 공포도보다 높거나 같다면
  if len(team_person) >= people[i]:
    # 팀 형성
    team += 1
    # 팀 그룹 초기화
    team_person = []
  else: 
    continue

print(team)
  
