// https://school.programmers.co.kr/learn/courses/30/lessons/181939

function solution(a, b) {
  let answer = 0;
  let str_a = a.toString();
  let str_b = b.toString();
  const ab = Number(str_a + str_b);
  const ba = Number(str_b + str_a);

  if (ab > ba) {
    answer = ab;
  } else {
    answer = ba;
  }

  return answer;
}
