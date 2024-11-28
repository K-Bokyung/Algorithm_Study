// https://school.programmers.co.kr/learn/courses/30/lessons/181890

function solution(str_list) {
  let answer = [];
  let l_idx = str_list.indexOf('l');
  let r_idx = str_list.indexOf('r');

  if (str_list.includes('l') && str_list.includes('r')) {
    l_idx < r_idx
      ? (answer = str_list.slice(0, l_idx))
      : (answer = str_list.slice(r_idx + 1, str_list.length));
  } else if (str_list.includes('l') && !str_list.includes('r')) {
    answer = str_list.slice(0, l_idx);
  } else if (!str_list.includes('l') && str_list.includes('r')) {
    answer = str_list.slice(r_idx + 1, str_list.length);
  }

  return answer;
}

const str_list = ['u', 'u', 'r', 'r'];
console.log(solution(str_list));
