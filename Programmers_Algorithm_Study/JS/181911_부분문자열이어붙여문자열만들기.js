// https://school.programmers.co.kr/learn/courses/30/lessons/181911

function solution(my_strings, parts) {
  let answer = '';
  let str_list = [];

  my_strings.forEach((item, index) => {
    let s = parts[index][0];
    let e = parts[index][1];
    let new_string = item.slice(s, e + 1);
    str_list.push(new_string);
  });

  answer = str_list.join('');

  return answer;
}
