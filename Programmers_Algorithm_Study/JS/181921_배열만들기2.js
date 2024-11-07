// https://school.programmers.co.kr/learn/courses/30/lessons/181921

function solution(l, r) {
  let answer = [];

  // 1. l과 r 사이에 있는 5의 배수 구하기
  for (i = l; i < r + 1; i++) {
    let str_num = '';

    if (i % 5 == 0) {
      str_num = i.toString().split('');

      // answer.push(str_num ? i : -1);

      console.log(i, str_num);
    }
  }

  return answer;
}

const l = 5;
const r = 55;
console.log(solution(l, r));
