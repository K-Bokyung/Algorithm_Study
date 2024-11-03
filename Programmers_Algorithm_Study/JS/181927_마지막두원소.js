// https://school.programmers.co.kr/learn/courses/30/lessons/181927

function solution(num_list) {
  let answer = [...num_list];
  let len = num_list.length;
  if (num_list[len - 1] > num_list[len - 2]) {
    result = num_list[len - 1] - num_list[len - 2];
    answer.push(result);
  } else {
    answer.push(num_list[len - 1] * 2);
  }

  console.log(num_list[len - 1]);

  return answer;
}
