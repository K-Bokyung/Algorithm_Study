//  https://school.programmers.co.kr/learn/courses/30/lessons/181938

function solution(a, b) {
  let answer = 0;
  const str_a = a.toString();
  const str_b = b.toString();
  const str_ab = Number(str_a + str_b);
  const ab = 2 * a * b;

  if (str_ab > ab) {
    answer = str_ab;
  } else {
    answer = ab;
  }

  return answer;
}

const a = 91;
const b = 2;
console.log(solution(a, b));
