// https://school.programmers.co.kr/learn/courses/30/lessons/181890

function solution(str_list) {
  let answer = [];
  let l_idx = 0;
  let r_idx = 0;

  if (str_list.includes('l') || str_list.includes('r')) {
    str_list.includes('l') ? (l_idx = str_list.indexOf('l')) : undefined;
    str_list.includes('r') ? (r_idx = str_list.indexOf('r')) : undefined;
  }

  l_idx > 0 && r_idx > 0 && l_idx < r_idx
    ? (answer = str_list.slice(0, l_idx))
    : (answer = str_list.slice(r_idx + 1, str_list.length));

  l_idx > 0 && r_idx === 0 ? (answer = str_list.slice(0, l_idx)) : undefined;
  l_idx === 0 && r_idx > 0 ? (answer = str_list.slice(r_idx + 1, str_list.length)) : undefined;

  l_idx === r_idx ? (answer = []) : undefined;

  return answer;
}

const str_list = ['u', 'l', 'l', 'u'];

console.log(solution(str_list));
