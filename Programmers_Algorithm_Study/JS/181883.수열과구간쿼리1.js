// https://school.programmers.co.kr/learn/courses/30/lessons/181883

function solution(arr, queries) {
  let answer = [...arr];

  queries.forEach((item) => {
    let s = item[0];
    let e = item[1];

    for (i = s; i < e + 1; i++) {
      answer[i] += 1;
    }
  });

  return answer;
}

const arr = [0, 1, 2, 3, 4];
const queries = [
  [0, 1],
  [1, 2],
  [2, 3],
];
console.log(solution(arr, queries));
