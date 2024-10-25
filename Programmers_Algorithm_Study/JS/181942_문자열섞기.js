// https://school.programmers.co.kr/learn/courses/30/lessons/181942

function solution(str1, str2) {
  let answer = [];
  let newStr1 = [...str1];
  let newStr2 = [...str2];
  let total_len = newStr1.length * 2;

  for (i = 0; i < total_len; i++) {
    if (i % 2 === 0) {
      answer.push(newStr1.shift());
    } else {
      answer.push(newStr2.shift());
    }
  }

  return answer.join('');
}

console.log(solution('aaaaa', 'bbbbb'));
