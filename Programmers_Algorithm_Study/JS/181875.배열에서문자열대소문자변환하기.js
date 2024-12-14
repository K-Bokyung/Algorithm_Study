// https://school.programmers.co.kr/learn/courses/30/lessons/181875

function solution(strArr) {
  let answer = [];
  strArr.map((item, index) => {
    index % 2 === 1 ? answer.push(item.toUpperCase()) : answer.push(item.toLowerCase());
  });

  return answer;
}

const strArr = ['AAA', 'BBB', 'CCC', 'DDD'];
console.log(solution(strArr));
