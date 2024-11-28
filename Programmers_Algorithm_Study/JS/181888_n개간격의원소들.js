// https://school.programmers.co.kr/learn/courses/30/lessons/181888

function solution(num_list, n) {
  let answer = [];

  for (i = 0; i < num_list.length; i += n) {
    answer.push(num_list[i]);
  }

  return answer;
}

const num_list = [4, 2, 6, 1, 7, 6];
const n = 4;
console.log(solution(num_list, n));
