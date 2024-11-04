// https://school.programmers.co.kr/learn/courses/30/lessons/181926

function solution(n, control) {
  let answer = n;
  let len_str = control.length;

  for (i = 0; i < len_str; i++) {
    if (control[i] == 'w') {
      answer += 1;
    } else if (control[i] == 's') {
      answer -= 1;
    } else if (control[i] == 'd') {
      answer += 10;
    } else {
      answer -= 10;
    }
  }

  return answer;
}
