// https://school.programmers.co.kr/learn/courses/30/lessons/181937

function solution(num, n) {
  let answer = 0;

  if (num % n === 0) {
    answer = 1;
  } else {
    answer = 0;
  }

  return answer;
}

const num = 34;
const n = 3;
console.log(solution(num, n));
