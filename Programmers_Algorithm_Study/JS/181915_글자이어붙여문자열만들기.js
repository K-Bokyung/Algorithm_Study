// https://school.programmers.co.kr/learn/courses/30/lessons/181915

function solution(my_string, index_list) {
  let answer = '';

  index_list.forEach((element) => {
    answer += my_string[element];
  });

  return answer;
}
