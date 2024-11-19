// https://school.programmers.co.kr/learn/courses/30/lessons/181903

function solution(q, r, code) {
  let answer = '';

  code.split('').forEach((item, index) => {
    if (index % q === r) {
      answer += item;
    }
  });

  return answer;
}
