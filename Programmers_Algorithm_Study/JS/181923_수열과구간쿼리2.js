// https://school.programmers.co.kr/learn/courses/30/lessons/181923

function solution(arr, queries) {
  let answer = [];

  for (i = 0; i < queries.length; i++) {
    console.log('i1', i);

    let query = queries[i];
    let s = query[0];
    let e = query[1];
    let k = query[2];
    let min_num = 0;

    for (i = s; i < e; i++) {
      console.log('i2', i);

      if (k < arr[i] && min_num == 0) {
        min_num = arr[i];
      } else if (k < arr[i] && arr[i] < min_num) {
        min_num = arr[i];
      } else if (i == e - 1 && min_num == 0) {
        min_num = -1;
      }

      answer.push(min_num);
    }
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
