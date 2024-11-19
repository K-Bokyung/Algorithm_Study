// https://school.programmers.co.kr/learn/courses/30/lessons/181902

function solution(my_string) {
  let answer = Array.from({ length: 52 }, (v, i) => (i = 0));
  let up_list = Array(26)
    .fill()
    .map((v, i) => String.fromCharCode(i + 65));
  let low_list = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 97));
  let total_list = up_list.concat(low_list);

  for (i = 0; i < my_string.length; i++) {
    answer[total_list.indexOf(my_string[i])] += 1;
  }

  return answer;
}
