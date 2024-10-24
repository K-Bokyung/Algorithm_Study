// https://school.programmers.co.kr/learn/courses/30/lessons/181943

function solution(my_string, overwrite_string, s) {
  let answer = [...my_string];
  const ws = overwrite_string;
  const ws_len = ws.length;

  answer.splice(s, ws_len, ws);

  return answer.join('');
}
