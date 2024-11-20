// https://school.programmers.co.kr/learn/courses/30/lessons/181900

function solution(my_string, indices) {
  let answer = '';

  my_string.split('').forEach((item, index) => {
    if (!indices.includes(index)) {
      answer += item;
    }
  });

  return answer;
}
