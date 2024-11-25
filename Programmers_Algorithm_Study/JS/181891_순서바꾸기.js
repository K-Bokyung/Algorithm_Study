// https://school.programmers.co.kr/learn/courses/30/lessons/181891

function solution(num_list, n) {
  let answer = [];
  let new_list = num_list.slice(n, num_list.length);

  answer = new_list.concat(num_list.splice(0, n));

  return answer;
}

const num_list = [5, 2, 1, 7, 5];
const n = 3;

console.log(solution(num_list, n));
