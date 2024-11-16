// https://school.programmers.co.kr/learn/courses/30/lessons/181905

function solution(my_string, s, e) {
  let answer = '';
  let slice_string = my_string
    .slice(s, e + 1)
    .split('')
    .reverse();
  let split_string = my_string.split('');

  split_string.splice(s, e - s + 1, ...slice_string);
  answer = split_string.join('');

  return answer;
}
