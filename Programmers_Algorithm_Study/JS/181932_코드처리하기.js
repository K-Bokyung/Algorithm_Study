// https://school.programmers.co.kr/learn/courses/30/lessons/181932

function solution(code) {
  let answer = '';
  let mode = 0;
  let ret = [];

  for (i = 0; i < code.length; i++) {
    if (code[i] == '1' && mode == '0') {
      mode = '1';
      continue;
    } else if (code[i] === '1' && mode == '1') {
      mode = '0';
      continue;
    }

    if (mode == '0' && i % 2 == 0) {
      ret.push(code[i]);
    }

    if (mode == '1' && i % 2 == 1) {
      ret.push(code[i]);
    }
  }

  if (ret.length == 0) {
    answer = 'EMPTY';
  } else {
    answer = ret.join('');
  }

  return answer;
}
