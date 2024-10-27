// https://school.programmers.co.kr/learn/courses/30/lessons/181936

function solution(number, n, m) {
  let answer = 0;

  if (number % n === 0 && number % m === 0) {
    answer = 1;
  } else {
    answer = 0;
  }

  return answer;
}
