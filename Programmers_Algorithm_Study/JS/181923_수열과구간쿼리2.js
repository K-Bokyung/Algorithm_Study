// https://school.programmers.co.kr/learn/courses/30/lessons/181923

function solution(arr, queries) {
  let answer = [];

  // 이전 풀이 (실패)
  // for (i = 0; i < queries.length; i++) {
  //   let query = queries[i];
  //   let s = query[0];
  //   let e = query[1];
  //   let k = query[2];

  //   let num_list = arr.slice(s, e + 1);
  //   num_list.forEach((item) => {
  //     if (k < item && answer.length < i + 1) {
  //       answer.push(item);
  //     } else if (k < item && answer.length == i + 1 && item < answer[i]) {
  //       answer[i] = item;
  //     } else if (item == num_list[e] && answer.length < i + 1) {
  //       answer.push(-1);
  //     }
  //   });
  // }

  // 재풀이
  for (let [s, e, k] of queries) {
    let num = arr.filter((item, idx) => idx >= s && idx <= e && item > k).sort((a, b) => a - b)[0];
    answer.push(num ? num : -1);
  }

  return answer;
}

const arr = [0, 1, 2, 4, 3];
const queries = [
  [0, 4, 2],
  [0, 3, 2],
  [0, 2, 2],
];
console.log(solution(arr, queries));
