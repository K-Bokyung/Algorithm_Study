//  https://school.programmers.co.kr/learn/courses/30/lessons/181922

function solution(arr, queries) {
  let answer = [...arr];

  for (let [s, e, k] of queries) {
    for (i = s; i <= e; i++) {
      if (i % k == 0) {
        answer[i] += 1;
      }
    }
  }

  return answer;
}
