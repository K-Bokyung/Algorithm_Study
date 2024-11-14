// https://school.programmers.co.kr/learn/courses/30/lessons/181912

function solution(intStrs, k, s, l) {
  let answer = [];

  intStrs.forEach((item) => {
    let new_strs = item.slice(s, s + l);
    new_strs > k ? answer.push(Number(new_strs)) : undefined;
  });

  return answer;
}
