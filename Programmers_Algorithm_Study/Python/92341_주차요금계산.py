# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    records_car = defaultdict(list)
    records_mon = defaultdict(int)
    
    # 1. records에서 시간, 차량번호, 내역을 딕셔너리로 정리
    for i in records:
      time, car_num, status = i.split()
      h, m = [int(j) for j in time.split(':')]
      min = h * 60 + m
      records_car[car_num].append(min)
    
    # 2. 각 차량 총 주차 시간 계산 후 딕셔너리로 정리
    for k, v in records_car.items():
      if len(v) % 2 == 1:
        v.append(23 * 60 + 59)
        
      park_time = 0
      
      for i, m in enumerate(v):
        if i % 2 == 0:
          park_time += v[i+1] - v[i]
      records_mon[k] = park_time

    # 3. 누적 주차 시간으로 주차 요금 계산
    answer = sorted(records_mon.items())
    for i in range(len(answer)):
      if answer[i][1] <= fees[0]:
        answer[i] = fees[1]
      else:
        answer[i] = fees[1] + (math.ceil((answer[i][1] - fees[0])/fees[2]) * fees[3])
    
    return answer
