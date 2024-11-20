// https://school.programmers.co.kr/learn/courses/30/lessons/181901

function solution(n, k) {
  let answer = [];
  let num = n / k;

  for (i = 1; i <= num; i++) {
    answer.push(k * i);
  }

  return answer;
}
