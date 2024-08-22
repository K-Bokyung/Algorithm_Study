# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = re.sub('[^a-z0-9-_.]+', '', new_id)
    
    # 3단계
    new_id = re.sub('[..]+', '.', new_id)
    
    # 4단계
    new_id = new_id.strip('.')
    
    # 5단계
    if new_id == '':
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 15:
        new_id = new_id[:15].strip('.')
    
    # 7단계
    if len(new_id) <= 2:
        n = 3 - len(new_id)
        new_id = new_id + new_id[-1]*n
    
    answer = new_id
    
    return answer
