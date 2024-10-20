# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    answer = 0
    num_list = []
    num = ""
    
    # 1. n을 k진수로 바꾸기
    while n:
      num = str(n % k) + num
      n = n // k
    
    num_list = [int(i) for i in num.split("0") if i != ""]
    
    # 2. 변환된 수 안에서 소수 찾기. 단, 0이 중간에 들어간 P는 제외.
    
    for i in num_list:
      prime = True
      
      if i < 2:
        continue
      
      # 소수인지 판별
      for j in range(2, int(i**0.5)+1):
        if i % j == 0:
          prime = False
          break
        
      if prime:
        answer += 1
    
    return answer
  