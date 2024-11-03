// https://school.programmers.co.kr/learn/courses/30/lessons/181928

function solution(num_list) {
  let answer = 0;
  let odd = '';
  let even = '';

  num_list.forEach((value) =>
    value % 2 == 1 ? (odd += value.toString()) : (even += value.toString())
  );

  answer = Number(odd) + Number(even);

  return answer;
}
