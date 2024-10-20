# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    total = []
    record_dict = {}
    
    # 1. record 리스트 요소들을 리스트로 변환
    record = [i.split(' ') for i in record]
    
    # 2. Enter, Leave, Change를 기준으로 total 리스트와 record_dict 딕셔너리에 값을 입력
    for i in record:
      # Enter
      if i[0] == 'Enter':
        record_dict[i[1]] = i[2]
        total.append(['Enter', i[1]])
      
      # Leave
      if i[0] == 'Leave':
        total.append(['Leave', i[1]])
      
      # Change
      if i[0] == 'Change':
        record_dict[i[1]] = i[2]
    
    # 3. 최종으로 answer에 문장 입력
    for i in total:
      # Enter
      if i[0] == 'Enter':
        name = record_dict[i[1]]
        answer.append(f'{name}님이 들어왔습니다.')
      
      # Leave
      if i[0] == 'Leave':
        name = record_dict[i[1]]
        answer.append(f'{name}님이 나갔습니다.')
    
    return answer