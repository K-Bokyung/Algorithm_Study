// https://school.programmers.co.kr/learn/courses/30/lessons/181924

function solution(arr, queries) {
  let answer = [...arr];
  let q_len = queries.length;

  for (i = 0; i < q_len; i++) {
    let a = queries[i][0];
    let b = queries[i][1];
    let a_num = answer[a];
    let b_num = answer[b];

    answer[a] = b_num;
    answer[b] = a_num;
  }

  return answer;
}
