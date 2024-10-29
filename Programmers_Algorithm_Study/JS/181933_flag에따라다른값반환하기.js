// https://school.programmers.co.kr/learn/courses/30/lessons/181933

function solution(a, b, flag) {
  let answer = 0;
  answer = flag == true ? a + b : a - b;

  return answer;
}
