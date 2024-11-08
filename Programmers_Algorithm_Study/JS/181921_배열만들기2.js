// https://school.programmers.co.kr/learn/courses/30/lessons/181921

function solution(l, r) {
  let answer = [];

  for (i = l; i < r + 1; i++) {
    let str_list = i.toString();

    if (![...str_list].every((item) => item === '5' || item === '0')) continue;
    answer.push(i);
  }

  if (answer.length == 0) {
    answer.push(-1);
  }

  return answer;
}
