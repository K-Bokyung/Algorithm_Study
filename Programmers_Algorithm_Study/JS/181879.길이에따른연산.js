// https://school.programmers.co.kr/learn/courses/30/lessons/181879

function solution(num_list) {
  let answer = 0;
  let sum = 0;
  let multi = 1;

  num_list.length >= 11
    ? (num_list.map((item) => (sum += item)), (answer = sum))
    : sum <= 10
    ? (num_list.map((item) => (multi *= item)), (answer = multi))
    : undefined;

  return answer;
}

const num_list = [2, 3, 4, 5];
console.log(solution(num_list));
