# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    result = []
    
    # 1. 4개 지표와 성격 유형 별 점수를 입력받을 공간 생성
    test_list = {
      'R': [0, 1],
      'T': [0, 1],
      'C': [0, 2],
      'F': [0, 2],
      'J': [0, 3],
      'M': [0, 3],
      'A': [0, 4],
      'N': [0, 5]
    }
    
    score_list = [0, 3, 2, 1, 0, 1, 2, 3]
    
    # 2. survey를 순회하면서 choices의 점수를 해당 유형에 더함
    for i in range(len(survey)):
      if choices[i] == 4:
        continue
      elif choices[i] < 4:
        test_list[survey[i][0]][0] += score_list[choices[i]]
      elif choices[i] > 4:
        test_list[survey[i][1]][0] += score_list[choices[i]]

    # 3. 4개 지표를 돌며 점수가 높은 유형을 차례대로 뽑음
    a = list(test_list.keys())
    list_i = [0, 2, 4, 6]
    list_j = [1, 3, 5, 7]
    
    for i in range(4):
        if test_list[(a[list_i[i]])][0] > test_list[a[list_j[i]]][0]:
          result.append(a[list_i[i]])
        elif test_list[(a[list_i[i]])][0] < test_list[a[list_j[i]]][0]:
          result.append(a[list_j[i]])
        elif test_list[(a[list_i[i]])][0] == test_list[a[list_j[i]]][0]:
          result.append(min(a[list_i[i]], a[list_j[i]]))
    
    # 4. 리스트 글자를 합쳐서 return
    answer = ''.join(result)
    
    return answer
