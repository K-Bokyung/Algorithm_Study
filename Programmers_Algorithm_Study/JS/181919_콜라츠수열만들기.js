// https://school.programmers.co.kr/learn/courses/30/lessons/181919

function solution(n) {
  let answer = [n];

  while (n !== 1) {
    if (n % 2 == 0) {
      n = n / 2;
    } else if (n % 2 == 1) {
      n = 3 * n + 1;
    }

    if (n !== 1) {
      answer.push(n);
    }
  }

  answer.push(1);

  return answer;
}
