// https://school.programmers.co.kr/learn/courses/30/lessons/181882

function solution(arr) {
  let answer = [];

  arr.forEach((item) => {
    if (item >= 50 && item % 2 === 0) {
      answer.push(item / 2);
    } else if (item < 50 && item % 2 === 1) {
      answer.push(item * 2);
    } else {
      answer.push(item);
    }
  });

  return answer;
}

const arr = [1, 2, 3, 100, 99, 98];
console.log(solution(arr));
