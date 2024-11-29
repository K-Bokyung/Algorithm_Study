// https://school.programmers.co.kr/learn/courses/30/lessons/181884

function solution(numbers, n) {
  let answer = 0;

  for (i = 0; i < numbers.length; i++) {
    if (answer > n) break;
    answer += numbers[i];
  }

  return answer;
}

const numbers = [58, 44, 27, 10, 100];
const n = 139;
console.log(solution(numbers, n));
