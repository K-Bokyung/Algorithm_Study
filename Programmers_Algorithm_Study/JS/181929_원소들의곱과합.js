// https://school.programmers.co.kr/learn/courses/30/lessons/181929

function solution(num_list) {
  let answer = 0;

  let total_sum = 0;
  num_list.forEach((value) => (total_sum += value));
  total_sum = total_sum ** 2;

  let each_sum = 1;
  num_list.forEach((value) => (each_sum *= value));

  if (each_sum < total_sum) {
    answer = 1;
  }

  return answer;
}
