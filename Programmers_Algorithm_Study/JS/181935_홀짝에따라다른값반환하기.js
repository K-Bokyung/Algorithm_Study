// https://school.programmers.co.kr/learn/courses/30/lessons/181935

function solution(n) {
  let answer = 0;

  if (n % 2 === 1) {
    for (i = n; i > 0; i -= 2) {
      answer += i;
    }
  } else if (n % 2 === 0) {
    for (i = n; i > 0; i -= 2) {
      answer += i ** 2;
    }
  }

  return answer;
}
