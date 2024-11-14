// https://school.programmers.co.kr/learn/courses/30/lessons/181910

function solution(my_string, n) {
  let answer = my_string.slice(-n, my_string.length);

  return answer;
}
