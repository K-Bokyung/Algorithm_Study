# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    
    # 1. 오늘 날짜 -> 숫자 -> 총 며칠인지 구하기
    today_num = list(map(int, today.split('.')))
    day_sum = today_num[0]*12*28 + today_num[1]*28 + today_num[2]
    
    # 2. 약관과 유효기간 -> 유효기간만 숫자로 -> 총 며칠인지 구하기
    terms_list = [[i.split(' ')[0], int(i.split(' ')[1])] for i in terms]
    for i in terms_list:
      days = i[1] * 28
      i[1] = days
    
    # 3. 수집된 개인정보 -> 수집 일자만 숫자로 -> 총 며칠인지 구하기
    privacies_list = [[list(map(int, i.split(' ')[0].split('.'))), (i.split(' ')[1])] for i in privacies]
    
    # 4. 수집한 날과 유효기간 일수를 리스트로 묶기
    defease_date = []
    
    for i in privacies_list:
      for j in terms_list:
        if i[1] == j[0]:
          days_list = i[0]
          days = days_list[0]*12*28 + days_list[1]*28 + days_list[2]
          total = days + j[1]
          defease_date.append(total)
    
    # 5. 유효기간 지났는지 체크
    for i in range(len(defease_date)):
      if day_sum >= defease_date[i]:
        answer.append(i+1)
    
    return answer
  
