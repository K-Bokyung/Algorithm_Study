// https://school.programmers.co.kr/learn/courses/30/lessons/181914

function solution(number) {
  let answer = 0;

  number.split('').forEach((element) => (answer += Number(element)));
  answer %= 9;

  return answer;
}
