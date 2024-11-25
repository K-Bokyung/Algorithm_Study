// https://school.programmers.co.kr/learn/courses/30/lessons/181892

function solution(num_list, n) {
  let answer = [];

  answer = num_list.splice(n - 1, num_list.length);

  return answer;
}

const num_list = [5, 2, 1, 7, 5];
const n = 2;

console.log(solution(num_list, n));
