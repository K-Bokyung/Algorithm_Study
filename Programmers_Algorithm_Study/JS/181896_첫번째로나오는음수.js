// https://school.programmers.co.kr/learn/courses/30/lessons/181896

function solution(num_list) {
  let answer = 0;
  let find_num = (item) => item < 0;

  if (num_list.findIndex(find_num)) {
    answer = num_list.findIndex(find_num);
  } else {
    answer = 0;
  }

  return answer;
}

const num_list = [12, 4, 15, 46, 38, -2, 15];
console.log(solution(num_list));
