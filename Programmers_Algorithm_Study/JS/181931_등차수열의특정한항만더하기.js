// https://school.programmers.co.kr/learn/courses/30/lessons/181931

function solution(a, d, included) {
  let answer = 0;
  let now_num = 0;
  let in_len = included.length;

  for (i = 0; i < in_len; i++) {
    if (included[i] == true) {
      now_num = i * d + a;
      answer += now_num;
    }
  }

  return answer;
}
