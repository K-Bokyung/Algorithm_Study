// https://school.programmers.co.kr/learn/courses/30/lessons/181898

function solution(arr, idx) {
  let answer = 0;
  let new_arr = arr.slice(idx, arr.length);

  if (new_arr.includes(1)) {
    answer = new_arr.indexOf(1) + idx;
  } else {
    answer = -1;
  }

  return answer;
}

const arr = [1, 1, 1, 1, 0];
const idx = 3;

console.log(solution(arr, idx));
