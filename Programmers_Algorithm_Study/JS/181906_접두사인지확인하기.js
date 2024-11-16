// https://school.programmers.co.kr/learn/courses/30/lessons/181906

function solution(my_string, is_prefix) {
  let answer = 0;
  let first_s = my_string[0];

  if (is_prefix[0] === first_s && is_prefix.length <= my_string.length) {
    is_prefix === my_string.slice(0, is_prefix.length) ? (answer = 1) : 0;
  }

  return answer;
}
