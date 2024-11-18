// https://school.programmers.co.kr/learn/courses/30/lessons/181904

function solution(my_string, m, c) {
  let answer = '';
  let str_list = [];

  for (i = 0; i < my_string.length; i += m) {
    let word = my_string.slice(i, i + m)[c - 1];
    str_list.push(word);
  }

  answer = str_list.join('');

  return answer;
}
