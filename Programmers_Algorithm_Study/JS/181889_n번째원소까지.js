// https://school.programmers.co.kr/learn/courses/30/lessons/181889

function solution(num_list, n) {
  let answer = [];
  answer = num_list.slice(0, n);

  return answer;
}

const num_list = [5, 2, 1, 7, 5];
const n = 3;
console.log(solution(num_list, n));
