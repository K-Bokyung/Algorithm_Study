// https://school.programmers.co.kr/learn/courses/30/lessons/181934

function solution(ineq, eq, n, m) {
  let answer = 0;

  if (ineq == '<' && eq == '=') {
    answer = n <= m ? 1 : 0;
  } else if (ineq == '<' && eq == '!') {
    answer = n < m ? 1 : 0;
  } else if (ineq == '>' && eq == '=') {
    answer = n >= m ? 1 : 0;
  } else if (ineq == '>' && eq == '!') {
    answer = n > m ? 1 : 0;
  }

  return answer;
}
