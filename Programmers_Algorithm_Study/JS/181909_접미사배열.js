// https://school.programmers.co.kr/learn/courses/30/lessons/181909

function solution(my_string) {
  let answer = [];
  let string_list = my_string.split('');
  let result = [my_string];

  for (i = 1; i < my_string.length; i++) {
    string_list.shift();
    let new_string = string_list.join('');
    result.push(new_string);
  }

  answer = result.sort();

  return answer;
}
