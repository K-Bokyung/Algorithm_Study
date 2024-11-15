// https://school.programmers.co.kr/learn/courses/30/lessons/181908

function solution(my_string, is_suffix) {
  let answer = 0;

  let string_list = my_string.split('');
  let suffixs = [my_string];

  for (i = 1; i < my_string.length; i++) {
    string_list.shift();
    let new_string = string_list.join('');
    suffixs.push(new_string);
  }

  suffixs.includes(is_suffix) ? (answer = 1) : (answer = 0);

  return answer;
}
