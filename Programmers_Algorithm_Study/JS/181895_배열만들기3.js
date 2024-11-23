// https://school.programmers.co.kr/learn/courses/30/lessons/181895

function solution(arr, intervals) {
  let answer = [];

  intervals.forEach((item) => {
    let a = item[0];
    let b = item[1];

    let new_arr = arr.slice(a, b + 1);
    answer.push(new_arr);
  });

  answer = answer[0].concat(answer[1]);

  return answer;
}

const arr = [1, 2, 3, 4, 5];
const intervals = [
  [1, 3],
  [0, 4],
];

console.log(solution(arr, intervals));
