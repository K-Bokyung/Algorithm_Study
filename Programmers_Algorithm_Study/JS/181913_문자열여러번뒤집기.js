// https://school.programmers.co.kr/learn/courses/30/lessons/181913

function solution(my_string, queries) {
  let answer = '';
  let new_string = my_string.split('');

  for (i = 0; i < queries.length; i++) {
    let s = queries[i][0];
    let e = queries[i][1];
    let reversed_str = new_string.slice(s, e + 1).reverse();
    new_string.splice(s, reversed_str.length, ...reversed_str);
  }

  answer = new_string.join('');

  return answer;
}
