// https://school.programmers.co.kr/learn/courses/30/lessons/181925

function solution(numLog) {
  let answer = '';
  let num_len = numLog.length - 1;

  for (i = 0; i < num_len; i++) {
    if (numLog[i] - numLog[i + 1] == -1) {
      answer += 'w';
    } else if (numLog[i] - numLog[i + 1] == 1) {
      answer += 's';
    } else if (numLog[i] - numLog[i + 1] == -10) {
      answer += 'd';
    } else {
      answer += 'a';
    }
  }

  return answer;
}
